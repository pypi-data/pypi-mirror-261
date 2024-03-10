from typing import List, Tuple, Optional
import json
import time
import logging
from typing import Final
from copy import deepcopy

from tenacity import (
    retry,
    stop_after_attempt,
    before_sleep_log,
)
from agentdesk import Desktop
from rich.console import Console
from rich.json import JSON

from .oai import chat
from .instruct import system_prompt, action_prompt, ActionSelection, reflection_prompt
from .util import remove_user_image_urls, clean_llm_json, shorten_user_image_urls
from guisurfer.agent import TaskAgent
from guisurfer.agent.task import Task

logger: Final = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

console = Console()


class DinOCR(TaskAgent):
    """A desktop agent that uses GPT-4V augmented with OCR and Grounding Dino to solve tasks"""

    def solve_task(
        self,
        task: Task,
        desktop: Desktop,
        max_steps: int = 10,
    ) -> Task:
        """Solve a task

        Args:
            task (Task): Task to solve
            desktop (Desktop): An AgentDesk desktop instance.
            max_steps (int, optional): Max steps to try and solve. Defaults to 5.

        Returns:
            Task: The task
        """

        if task.url:
            console.print(f"opening site url: {task.url}", style="blue")
            desktop.open_url(task.url)
            console.print("waiting for browser to open...", style="blue")
            time.sleep(5)

        desktop.move_mouse(500, 500)
        tools = desktop.json_schema()
        console.print("\ntools: ", style="purple")
        console.print(JSON.from_data(tools))

        info = desktop.info()
        screen_size = info["screen_size"]

        msgs = []
        msg = {
            "role": "system",
            "content": [{"type": "text", "text": system_prompt(tools, screen_size)}],
        }
        msgs.append(msg)

        response = chat(msgs)
        console.print(f"\nsystem prompt response: {response}", style="blue")
        msgs.append(response)

        for i in range(max_steps):
            console.print(f"\n\n-------\n\nstep {i + 1}\n", style="green")

            msgs, done = self.take_action(desktop, task, msgs, screen_size)

            if done:
                console.print("task is done", style="green")
                # TODO: remove
                time.sleep(10)
                return msgs

            time.sleep(2)
            # input("Press Enter to continue to the next step...")

        console.print("Reached max steps without solving task", style="red")

    @retry(
        stop=stop_after_attempt(5),
        before_sleep=before_sleep_log(logger, logging.INFO),
    )
    def take_action(
        self, desktop: Desktop, task: Task, msgs: List, screen_size: dict
    ) -> Tuple[List, bool]:
        """Take an action

        Args:
            desktop (Desktop): Desktop to use
            task (str): Task to accomplish
            msgs (List): Messages for the task
            screen_size (dict): Size of the screen

        Returns:
            bool: Whether the task is complete
        """
        console.print("taking action...", style="white")

        _msgs = deepcopy(msgs)
        _msgs = remove_user_image_urls(_msgs)

        screenshot_b64 = desktop.take_screenshot()

        x, y = desktop.mouse_coordinates()
        console.print(f"mouse coordinates: ({x}, {y})", style="white")

        msg = action_prompt(task, screenshot_b64, x, y, screen_size)
        _msgs.append(msg)

        logging.debug("calling chat with msgs")
        # logging.debug(pprint.pprint(shorten_user_image_urls(deepcopy(_msgs))))

        response = chat(_msgs)
        # console.print(f"\ngpt response: {response}", style="blue")

        try:
            cleaned_content = clean_llm_json(response["content"])
            jdict = json.loads(cleaned_content)

            selection = ActionSelection(**jdict)
            console.print(f"\naction selection: ", style="white")
            console.print(JSON.from_data(jdict))

        except Exception as e:
            console.print(f"Response failed to parse: {e}", style="red")
            raise

        if selection.action.name == "result":
            # Need some reflection - is the task solved?
            console.print(
                "Received a final result candidate, reflecting on if the job is done...",
                style="green",
            )
            rprompt = reflection_prompt(
                task, selection.action.parameters["value"], screenshot_b64
            )
            logging.debug("reflect prompt: ", rprompt)

            _msgs.append(rprompt)
            reflect_response = chat([rprompt])
            logging.debug("reflect response: ", reflect_response)

            _msgs.append(reflect_response)
            reflect_dict = json.loads(reflect_response["content"])
            logging.debug("reflect dict: ", reflect_dict)

            if reflect_dict["finished"] == "yes":
                console.print("\nfinished!", style="green")
                console.print("final result: ", style="green")
                console.print(JSON.from_data(selection.action.parameters))
                return _msgs, True
            else:
                console.print("\nnot finished yet...", style="yellow")
                return _msgs, False

        action = desktop.find_action(selection.action.name)
        console.print(f"found action: {action}", style="blue")
        if not action:
            console.print(f"\naction returned not found: {selection.action.name}")
            raise SystemError("action not found")

        try:
            action_response = desktop.use(action, **selection.action.parameters)
        except Exception as e:
            raise ValueError(f"Trouble using action: {e}")

        console.print(f"action output: {action_response}", style="blue")

        _msgs.append(response)
        return _msgs, False
