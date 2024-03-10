import base64
from io import BytesIO
from typing import Union, Tuple, List, Dict, Any
import json
import re

from PIL import Image, ImageDraw, ImageFont


def visualize_b64_img(b64_str: str) -> Union[Image.Image, None]:
    try:
        img_data = base64.b64decode(b64_str)
        img_io = BytesIO(img_data)
        img = Image.open(img_io)

        return img
    except Exception as e:
        print(f"Error loading image: {e}")
        return None


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def reduce_image_resolution(b64_str: str, target_size: Tuple[int, int]) -> str:
    """
    Reduces the resolution of a base64-encoded image using the LANCZOS resampling filter.
    """
    # Decode the base64 string to bytes
    img_data: bytes = base64.b64decode(b64_str)
    img: Image.Image = Image.open(BytesIO(img_data))

    # Resize the image using LANCZOS resampling
    resized_img: Image.Image = img.resize(target_size, Image.Resampling.LANCZOS)

    # Convert the resized image back to a base64 string
    buffer: BytesIO = BytesIO()
    resized_img.save(buffer, format=img.format)
    new_b64_str: str = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return new_b64_str


def remove_user_image_urls(messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:

    ret = []
    for message in messages:
        # Check if the message role is 'user'
        if not message:
            continue

        if message.get("role") == "user":
            new_content = []
            for content_piece in message.get("content", []):
                # Exclude 'image_url' objects
                if content_piece.get("type") != "image_url":
                    new_content.append(content_piece)
            message["content"] = new_content

        ret.append(message)

    return ret


def shorten_user_image_urls(messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:

    ret = []
    for message in messages:
        # Check if the message role is 'user'
        if not message:
            continue

        if message.get("role") == "user":
            new_content = []
            for content_piece in message.get("content", []):
                # Exclude 'image_url' objects
                if content_piece.get("type") == "image_url":
                    content_piece["image_url"][
                        "url"
                    ] = f"{content_piece['image_url']['url'][:10]}..."
                new_content.append(content_piece)

            message["content"] = new_content

        ret.append(message)

    return ret


def clean_llm_json(input_text: str) -> str:
    cleaned_text = input_text.replace("```", "")

    if cleaned_text.startswith("json\n"):
        cleaned_text = cleaned_text.replace("json\n", "", 1)

    return cleaned_text.strip()


def visualize_bounding_boxes(
    input_image: str, image_data: List[List[int]], coordinates: List[List[int]]
) -> None:
    """
    Visualizes bounding boxes and coordinates on the original image.

    Args:
    - input_image (str): Path to the original image file.
    - image_data (List[List[int]]): List of bounding boxes [x_min, y_min, x_max, y_max] to draw on the image.
    - coordinates (List[List[int]]): List of extended boxes [x_min, y_min, x_max, y_max] to draw on the image.
    """
    image = Image.open(input_image)
    draw = ImageDraw.Draw(image)

    # Draw bounding boxes from image_data
    for bbox in image_data:
        draw.rectangle(bbox, outline="red", width=2)

    # Draw coordinate boxes from coordinates
    for coord in coordinates:
        draw.rectangle(coord, outline="blue", width=2)

    # Display the result or save to file
    image.save(
        "./temp/result_with_boxes.png"
    )  # Or use image.save("result_with_boxes.png") to save the file


def extract_parse_json(input_str: str) -> Union[dict, str]:
    """
    Extracts and parses a JSON object from the input string using regex if it is tagged with 'json\n'
    and enclosed in backticks, otherwise returns the input string.

    :param input_str: A string that may contain a JSON object.
    :return: A dictionary if JSON is parsed, otherwise the original string.
    """
    # Regex to match 'json\n{...}' pattern enclosed in backticks
    match = re.search(r"```json\n([\s\S]+?)\n```", input_str)
    if match:
        json_str = match.group(1)  # Extract the JSON string
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            return "Invalid JSON format."
    else:
        return json.loads(input_str)


def combine_images_vertically(image_paths: List[str], output_path: str) -> None:
    """Combine images to present them to GPT"""
    images = [Image.open(path) for path in image_paths]
    padding = 10
    line_height = 2
    total_height = sum(image.height + padding * 2 for image in images) + line_height * (
        len(images) - 1
    )
    max_width = max(image.width for image in images) + 100

    combined_image = Image.new("RGB", (max_width, total_height), "white")
    draw = ImageDraw.Draw(combined_image)

    # Attempt to use a larger font; adjust the path as necessary
    try:
        font = ImageFont.truetype("./font/arial.ttf", 36)
    except IOError:
        font = ImageFont.load_default()
        print("Fallback to default font.")

    y_offset = 0
    for index, image in enumerate(images):
        new_y_offset = y_offset + padding
        combined_image.paste(image, (100, new_y_offset))
        draw.text(
            (20, new_y_offset + image.height // 2 - 18),
            str(index),
            fill="black",
            font=font,
        )
        y_offset = new_y_offset + image.height + padding
        if index < len(images) - 1:
            draw.line(
                [(0, y_offset), (max_width, y_offset)], fill="black", width=line_height
            )
            y_offset += line_height

    combined_image.save(output_path)
