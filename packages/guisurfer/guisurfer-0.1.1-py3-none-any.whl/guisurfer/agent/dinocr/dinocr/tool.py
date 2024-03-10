import base64
from typing import Union, List, Optional
import os
from io import BytesIO
import time
import logging

from PIL import Image, ImageDraw
from agentdesk import Desktop
from opentool import Action, action, Observation
from MobileAgent.icon_localization import load_model, det
from MobileAgent.crop import crop, crop_for_clip, clip_for_icon
from MobileAgent.text_localization import ocr
import clip
import requests
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from agentdesk.vm.base import DesktopVM, DesktopProvider
from agentdesk.vm.qemu import QemuProvider
from rich.console import Console

try:
    from agentdesk.vm.gce import GCEProvider
except ImportError:
    print(
        "GCE provider unavailable, install with `pip install agentdesk[gce] if desired"
    )
try:
    from agentdesk.vm.ec2 import EC2Provider
except ImportError:
    print(
        "AWS provider unavailable, install with `pip install agentdesk[aws] if desired"
    )


from .oai import chat
from .instruct import (
    text_img_prompt,
    system_prompt,
    action_prompt,
    select_icon_prompt_composite,
)
from .util import (
    visualize_bounding_boxes,
    extract_parse_json,
    combine_images_vertically,
)

# TODO: this is just for demo
import warnings

# Suppress specific warnings
warnings.filterwarnings(
    "ignore",
    message="The `device` argument is deprecated and will be removed in v5 of Transformers.",
)
warnings.filterwarnings(
    "ignore",
    message="torch.utils.checkpoint: please pass in use_reentrant=True or use_reentrant=False explicitly.",
)
warnings.filterwarnings(
    "ignore",
    message="None of the inputs have requires_grad=True. Gradients will be None",
)


console = Console()


class SemanticDesktop(Desktop):
    """A semantic desktop replaces click actions with semantic description rather than coordinates"""

    def __init__(
        self,
        agentd_url: Optional[str] = None,
        vm: Optional[DesktopVM] = None,
        storage_uri: str = "file://.media",
        type_min_interval: float = 0.05,
        type_max_interval: float = 0.25,
        move_mouse_duration: float = 1.0,
        mouse_tween: str = "easeInOutQuad",
        store_img: bool = False,
        requires_proxy: bool = False,
        proxy_type: str = "process",
        proxy_port: int = 8000,
    ) -> None:
        """
        Initialize and open a URL in the application.

        Args:
            url: URL to open upon initialization.
            agentd_url: URL of a running agentd server. Defaults to None.
            vm: Optional desktop VM to use. Defaults to None.
            storage_uri: The directory where to store images or videos taken of the VM, supports gs:// or file://. Defaults to "file://.media".
            type_min_interval: Min interval between pressing the next key. Defaults to 0.05.
            type_max_interval: Max interval between pressing the next key. Defaults to 0.25.
            move_mouse_duration: How long it should take to move the mouse. Defaults to 1.0.
            mouse_tween: The movement tween. Defaults to "easeInOutQuad".
            store_img: Whether to store the image in the cloud. Defaults to False.
            requires_proxy: Whether the VM requires a proxy to access the internet. Defaults to False.
            proxy_type: The type of proxy to use. Defaults to "process".
            proxy_port: The port to use for the proxy. Defaults to 8000.
        """
        super().__init__(
            agentd_url=agentd_url,
            vm=vm,
            storage_uri=storage_uri,
            type_min_interval=type_min_interval,
            type_max_interval=type_max_interval,
            move_mouse_duration=move_mouse_duration,
            mouse_tween=mouse_tween,
            store_img=store_img,
            requires_proxy=requires_proxy,
            proxy_type=proxy_type,
            proxy_port=proxy_port,
        )

        device = "cpu"
        config_file: str = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "dino_config.py"
        )
        model_filename = "groundingdino_swint_ogc.pth"
        ckpt_filename: str = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), model_filename
        )
        console.print(f"Loading Grounding Dino model...", style="green")
        self._ensure_download(
            "https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth",
            ckpt_filename,
        )

        self.groundingdino_model = load_model(
            config_file, ckpt_filename, device=device
        ).eval()

        # console.print(f"Loading CLIP model...", style="green")
        # self.clip_model, self.clip_preprocess = clip.load("ViT-B/32", device=device)

        console.print(f"Loading OCR model...", style="green")
        self.ocr_detection = pipeline(
            Tasks.ocr_detection, model="damo/cv_resnet18_ocr-detection-line-level_damo"
        )
        self.ocr_recognition = pipeline(
            Tasks.ocr_recognition,
            model="damo/cv_convnextTiny_ocr-recognition-document_damo",
        )
        self.session_data = {}
        os.makedirs("./.img", exist_ok=True)
        os.makedirs("./temp", exist_ok=True)

    def _add_session_data(self, key: str, value: str) -> None:
        """Add data to the session"""
        self.session_data[key] = value

    def _ensure_download(self, url: str, local_filename: str) -> None:
        """
        Download a file from `url` if it does not already exist and save it locally under `local_filename`.
        """
        if not os.path.exists(local_filename):
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                with open(local_filename, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            print(f"Downloaded {local_filename}")
        else:
            print(f"{local_filename} already exists. No download needed.")

    def _click_coords(self, x: int, y: int, button: str = "left") -> None:
        """Click mouse button

        Args:
            button (str, optional): Button to click. Defaults to "left".
            x (Optional[int], optional): X coordinate to move to, if not provided it will click on current location. Defaults to None.
            y (Optional[int], optional): Y coordinate to move to, if not provided it will click on current location. Defaults to None.
        """
        # TODO: fix click cords in agentd
        logging.debug("moving mouse")
        body = {"x": int(x), "y": int(y)}
        resp = requests.post(f"{self.base_url}/move_mouse", json=body)
        resp.raise_for_status()
        time.sleep(2)

        logging.debug("clicking")
        resp = requests.post(f"{self.base_url}/click", json={})
        resp.raise_for_status()
        time.sleep(2)
        return

    def actions(self) -> List[Action]:
        """Actions the agent can take

        Returns:
            List[Action]: List of actions
        """
        out = []
        for action in self._actions_list:
            if action.name in [
                "open_url",
                "type_text",
                "click_text",
                "click_icon",
                "scroll",
                "press_key",
                "result",
            ]:
                out.append(action)

        return out

    def observations(self) -> List[Observation]:
        """Observations the agent can make

        Returns:
            List[Observation]: List of observations
        """
        return []

    @action
    def click_text(self, text: str) -> None:
        """Click on a piece of text

        Args:
            text (str): The exact text you want to click
        """

        logging.debug("clicking text: ", text)
        info = self.info()
        x, y = info["screen_size"]["x"], info["screen_size"]["y"]
        logging.debug(f"Screen size is x: {x} y: {y}")
        b64_img = self.take_screenshot()

        image_path = "./.img/current.png"
        self._save_b64_image(b64_img, image_path)
        iw, ih = Image.open(image_path).size
        logging.debug("iw, ih:", iw, ih)

        in_coordinate, out_coordinate = ocr(
            image_path, text, self.ocr_detection, self.ocr_recognition, iw, ih
        )
        logging.debug("in_coordinate: ", in_coordinate)
        logging.debug("out_coordinate: ", out_coordinate)

        # if no instances of the specified text were found in the screenshot.
        if len(out_coordinate) == 0:
            raise SystemError(
                f'Failed to execute action click text ({text}). The text "{text}" is not detected in the screenshot.'
            )

        # Check if there are more than four instances of the specified text, indicating ambiguity.
        elif len(out_coordinate) > 4:
            raise SystemError(
                f'Failed to execute action click text ({text}). There are too many text "{text}" in the screenshot.'
            )

        # If exactly one instance of the specified text is found, proceed to calculate the tap coordinates.
        elif len(out_coordinate) == 1:
            logging.debug("one instance")
            logging.debug("box: ", in_coordinate)
            tap_coordinate = [
                (in_coordinate[0][0] + in_coordinate[0][2]) / 2,
                (in_coordinate[0][1] + in_coordinate[0][3]) / 2,
            ]

            logging.debug("coord: ", tap_coordinate)
            logging.debug("iw and ih: ", iw, ih)
            logging.debug("clicking on text: ", tap_coordinate[0], tap_coordinate[1])
            self._click_coords(x=tap_coordinate[0], y=tap_coordinate[1])

        # If there are multiple but fewer than five instances of the text, handle the ambiguity.
        else:
            logging.debug("multiple instances")
            hash = {}
            for i, (td, box) in enumerate(zip(in_coordinate, out_coordinate)):
                crop(image_path, box, i + 1, td)
                hash[i + 1] = td

            images = []
            temp_file = "./temp"
            for i in range(len(hash.keys())):
                crop_image = f"{i+1}.jpg"
                images.append(os.path.join(temp_file, crop_image))

            msgs = []
            msgs.append(system_prompt(self.json_schema(), info["screen_size"]))
            msgs.append(
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": "Okay send me the first screenshot when you are ready.",
                        },
                    ],
                }
            )
            x, y = self.mouse_coordinates()
            task = self.session_data.get("task", None)
            msgs.append(
                action_prompt(
                    task,
                    b64_img,
                    x,
                    y,
                    screen_size=info["screen_size"],
                    grid=False,
                )
            )
            msgs.append(
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": '{"reason": "I need to click on the text that looks like \''
                            + text
                            + '\'", "action": {"name": "click_text", "parameters": {"description": "'
                            + text
                            + '"}}}',
                        },
                    ],
                }
            )
            ocr_prompt = (
                f"I need some clarification on the last step. The {str(len(out_coordinate))} red boxes are numbered"
                f' 1 through {str(len(out_coordinate))}. Which red box with "{text}" do you want to click on?'
                f"Please output just one number from 1 to {str(len(out_coordinate))}, such as 1, 2......",
            )
            ocr_msg = text_img_prompt("user", ocr_prompt, images)
            msgs.append(ocr_msg)
            choose_response = chat(msgs)
            logging.debug("clarify response: ", choose_response)

            final_box = hash[int(choose_response["content"])]
            tap_coordinate = [
                (final_box[0] + final_box[2]) / 2,
                (final_box[1] + final_box[3]) / 2,
            ]
            logging.debug("coord: ", tap_coordinate)
            logging.debug("iw and ih: ", iw, ih)
            logging.debug("clicking on text: ", tap_coordinate[0], tap_coordinate[1])
            self._click_coords(x=tap_coordinate[0], y=tap_coordinate[1])

    @action
    def click_icon(self, description: str, approx_loc: str) -> None:
        """Click on an icon

        Args:
            description (str): The description of the icon, for example "a round dark blue icon with the text 'Home'", please be a generic as possible
            approx_loc (str): Approximate location of the icon, options are "top", "bottom", "left", "right", "center". Please choose one option
        """
        logging.debug(
            "clicking icon with description and location: ", description, approx_loc
        )
        info = self.info()
        x, y = info["screen_size"]["x"], info["screen_size"]["y"]
        logging.debug("image size: ", x, y)

        b64_img = self.take_screenshot()

        image_path = "./.img/current.png"
        self._save_b64_image(b64_img, image_path)
        iw, ih = Image.open(image_path).size
        logging.debug("image size: ", iw, ih)

        in_coordinate, out_coordinate = det(
            image_path, "icon", self.groundingdino_model
        )
        logging.debug("in_coordinate: ", in_coordinate)
        logging.debug("out_coordinate: ", out_coordinate)
        visualize_bounding_boxes(image_path, in_coordinate, out_coordinate)

        # There is only one icon
        if len(out_coordinate) == 1:
            logging.debug("one instance")
            logging.debug("box: ", in_coordinate)
            tap_coordinate = [
                (in_coordinate[0][0] + in_coordinate[0][2]) / 2,
                (in_coordinate[0][1] + in_coordinate[0][3]) / 2,
            ]
            logging.debug("coord: ", tap_coordinate)
            logging.debug("clicking on icon: ", tap_coordinate[0], tap_coordinate[1])
            self._click_coords(x=tap_coordinate[0], y=tap_coordinate[1])

        # There are multiple icons, do a similarity search to the description
        else:
            logging.debug("multiple instances")
            temp_file = "./temp"
            hash = []
            clip_filter = []
            for i, (td, box) in enumerate(zip(in_coordinate, out_coordinate)):
                logging.debug("\ncrop_for_clip clip: ", td, box)
                if crop_for_clip(image_path, td, i + 1, approx_loc):
                    hash.append(td)
                    crop_image = f"{i+1}.jpg"
                    clip_filter.append(os.path.join(temp_file, crop_image))

            combine_images_vertically(clip_filter, "./temp/all_icons.jpg")

            prompt = select_icon_prompt_composite(description, "./temp/all_icons.jpg")
            response = chat([prompt])
            logging.debug("GPT response:", response)
            resp = extract_parse_json(response["content"])
            logging.debug("Parsed response:", resp)

            if "index" not in resp:
                raise ValueError(f"'index' not in response: {resp}")
            selected_index = resp["index"]

            final_box = hash[selected_index]
            logging.debug("final box: ", final_box)
            logging.debug("final img path: ", clip_filter[selected_index])
            self._draw_box_on_b64_image(b64_img, final_box)

            click_coordinate = [
                (final_box[0] + final_box[2]) / 2,
                (final_box[1] + final_box[3]) / 2,
            ]
            logging.debug("click coord: ", click_coordinate)
            logging.debug(
                "clicking on icon: ", click_coordinate[0], click_coordinate[1]
            )
            self._click_coords(x=click_coordinate[0], y=click_coordinate[1])

            b64_new = self.take_screenshot()
            image_data = base64.b64decode(b64_new)
            image = Image.open(BytesIO(image_data))
            image.save("./temp/post_action_screenshot.png")
            return

    def _draw_box_on_b64_image(self, b64_img: str, box_coordinates: tuple) -> None:
        """
        Draws a box on a base64-encoded image using the provided coordinates and saves the image.

        Args:
            b64_img (str): The base64-encoded image.
            box_coordinates (tuple): A tuple of coordinates (x_min, y_min, x_max, y_max) for the box.
        """
        # Decode the base64 image
        img_data = base64.b64decode(b64_img)
        image = Image.open(BytesIO(img_data))

        # Draw the rectangle on the image
        draw = ImageDraw.Draw(image)
        draw.rectangle(box_coordinates, outline="red", width=3)

        # Save the image with the box
        image.save("./temp/final_box.png")

    def _save_b64_image(self, b64_string: str, file_path: str) -> Union[bool, str]:
        try:
            image_data = base64.b64decode(b64_string)
            with open(file_path, "wb") as file:
                file.write(image_data)
            return True
        except Exception as e:
            return str(e)

    @classmethod
    def ensure(
        cls,
        name: str,
        provider: DesktopProvider = QemuProvider(),
        image: Optional[str] = None,
        memory: int = 4,
        cpus: int = 2,
        disk: str = "30gb",
        reserve_ip: bool = False,
        ssh_key: Optional[str] = None,
    ) -> "SemanticDesktop":
        """Find or create a desktop"""
        vm = DesktopVM.find(name)
        if vm:
            return cls.from_vm(vm)

        return cls.create(
            name, provider, image, memory, cpus, disk, reserve_ip, ssh_key
        )

    @classmethod
    def create(
        cls,
        name: Optional[str] = None,
        provider: DesktopProvider = QemuProvider(),
        image: Optional[str] = None,
        memory: int = 4,
        cpus: int = 2,
        disk: str = "30gb",
        reserve_ip: bool = False,
        ssh_key: Optional[str] = None,
    ) -> "SemanticDesktop":
        """Create a desktop VM"""
        vm = provider.create(name, image, memory, cpus, disk, reserve_ip, ssh_key)
        return cls.from_vm(vm)

    @classmethod
    def from_vm(cls, vm: DesktopVM) -> "SemanticDesktop":
        """Create a desktop from a VM

        Args:
            vm (DesktopVM): VM to use

        Returns:
            Desktop: A desktop
        """
        return SemanticDesktop(vm=vm)

    @classmethod
    def ec2(
        cls,
        name: Optional[str] = None,
        region: Optional[str] = None,
        image: Optional[str] = None,
        memory: int = 4,
        cpus: int = 2,
        disk: str = "30gb",
        reserve_ip: bool = False,
        ssh_key: Optional[str] = None,
    ) -> "SemanticDesktop":
        """Create a desktop VM on EC2"""
        return cls.create(
            name=name,
            provider=EC2Provider(region),
            image=image,
            memory=memory,
            cpus=cpus,
            disk=disk,
            reserve_ip=reserve_ip,
            ssh_key=ssh_key,
        )

    @classmethod
    def gce(
        cls,
        name: Optional[str] = None,
        project: Optional[str] = None,
        zone: Optional[str] = None,
        image: Optional[str] = None,
        memory: int = 4,
        cpus: int = 2,
        disk: str = "30gb",
        reserve_ip: bool = False,
        ssh_key: Optional[str] = None,
    ) -> "SemanticDesktop":
        """Create a desktop VM on GCE"""
        return cls.create(
            name=name,
            provider=GCEProvider(project, zone),
            image=image,
            memory=memory,
            cpus=cpus,
            disk=disk,
            reserve_ip=reserve_ip,
            ssh_key=ssh_key,
        )

    @classmethod
    def local(
        cls,
        name: Optional[str] = None,
        memory: int = 4,
        cpus: int = 2,
    ) -> "SemanticDesktop":
        """Create a local VM

        Args:
            name (str, optional): Name of the vm. Defaults to None.
            memory (int, optional): Memory the VM has. Defaults to 4.
            cpus (int, optional): CPUs the VM has. Defaults to 2.

        Returns:
            Desktop: A desktop
        """
        return cls.create(name=name, provider=QemuProvider(), memory=memory, cpus=cpus)
