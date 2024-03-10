from __future__ import annotations
from typing import Dict, Any, List
import json
import base64

from pydantic import BaseModel

from agentdesk.processors.grid import GridProcessor
from .util import encode_image


class Action(BaseModel):
    """An action"""

    name: str
    parameters: Dict[str, Any]


class ActionSelection(BaseModel):
    """An action selection from the model"""

    reason: str
    action: Action


def system_prompt(
    actions: Dict[str, Any],
    screen_size: Dict[str, int],
    max_steps: int = 5,
    grid: bool = False,
) -> str:
    """Generate the system prompt

    Args:
        actions (Dict[str, Any]): Actions to select from
        screen_size (Dict[str, int]): Size of the screen (w, h)
        max_steps (int, optional): Max steps. Defaults to 5.
        grid (bool): Whether the image has a grid overlay. Defaults to False

    Returns:
        str: The system prompt
    """
    acts = json.dumps(actions, indent=4)

    query = f"""You are using a computer, you have access to a mouse and keyboard. 
I'm going to show you the picture of the screen along with the current mouse coordinates."""

    if grid:
        query += (
            "I will also give you another picture of the screen with a grid overlaying it where each square is 100px by 100px,"
            "the coordinates of each line intersection are written below it. You can use that to better guage how to move."
        )

    query += f"""
The screen size is ({screen_size["x"]}, {screen_size["y"]})

We will then select from a set of actions:

"""
    query += acts
    query += """ 

You will return the action in the form of:
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "reason": {
            "type": "string"
        },
        "action": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "parameters": {
                    "type": "object",
                    "additionalProperties": true
                }
            },
            "required": ["name", "parameters"]
        }
    },
    "required": ["reason", "function"]
}

For example, if we need to move to a search bar located at (400, 500) you would return:
{
    "reason": "I need to click on the google search bar",
    "action": {
        "name": "click_icon",
        "parameters": {"description": "Google search bar", "approx_loc": "center"},
    },
}

If the task is finished, please return the action name 'result', with the parameters of any output that may be needed from the task.
For example, if my task is to 'Search for breeds of irish dogs' and I need to give the user the results, I would return:
{
    "reason": "I need to return the results of the search",
    "action": {
        "name": "result",
        "parameters": {"value": "Irish Setter, Irish Wolfhound, Irish Terrier, Irish Water Spaniel"},
    },
}

Please be concise and return just the raw valid JSON, the output should be directly parsable as JSON

Okay, when you are ready I'll send you the current screenshot and mouse coordinates.
"""
    return query


def action_prompt(
    task: str,
    screenshot_b64: str,
    x: int,
    y: int,
    screen_size: Dict[str, int],
    grid: bool = False,
) -> dict:
    """Generate an action prompt

    Args:
        task (str): Task to generate the prompt for
        screenshot_b64 (str): b64 encoded screenshot
        x (int): The X coordinate of the mouse
        y (int): They Y coordinate of the mouse
        screen_size (Dict[str, int]): The (w, h) screen size.
        grid (bool): Whether the image has a grid overlay. Defaults to False.

    Returns:
        dict: An openai formatted message
    """
    if grid:
        gp = GridProcessor()
        screenshot_b64_grid = gp.process_b64(screenshot_b64)

    msg = {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": (
                    f"Current mouse coordinates are ({x}, {y}), the screen size is ({screen_size['x']}, {screen_size['y']})"
                    f" and the task to solve is '{task}', please return the appropriate next action as raw JSON. Please review your "
                    "last action carefully and see if the current screenshot reflects what you hoped to accomplish, is the cursor in the right"
                    " location? Does the screen look correct?"
                ),
            },
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{screenshot_b64}"},
            },
        ],
    }
    if grid:
        msg["content"].append(
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{screenshot_b64_grid}"},
            }
        )
    return msg


def text_img_prompt(
    role: str, prompt: str, images: List[str], format: str = "jpeg"
) -> dict:

    content = [
        {"type": "text", "text": prompt},
    ]
    for image in images:
        base64_image = encode_image(image)
        img_content = {
            "type": "image_url",
            "image_url": {"url": f"data:image/{format};base64,{base64_image}"},
        }
        content.append(img_content)

    msg = {"role": "user", "content": [content]}
    return msg


def reflection_prompt(task: str, result: str, screenshot_b64: str) -> dict:

    prompt = (
        f"""Given the task '{task}' and the provided image, is it solved by the result '{result}'?"""
        + """
Please return a 'yes' or 'no' response indicating if the result matches the task objective. And a reason as to why it does or doesn't.

Here is an example of a good result
{
    "reason": "The task 'Search for types of Canadian sheep' is solved by the result 'Suffolk, Dorset, and Rideau Arcott' ",
    "finished": "yes"
}

Here is an example of a bad result:
{
    "reason": "The task 'Search for types of Canadian sheep' is not solved by the result 'Peter pan' because that is not a type of sheep",
    "finished": "no"
}
"""
    )
    content = [
        {
            "type": "text",
            "text": prompt,
        },
    ]
    img_content = {
        "type": "image_url",
        "image_url": {"url": f"data:image/png;base64,{screenshot_b64}"},
    }
    content.append(img_content)

    msg = {"role": "user", "content": content}
    return msg


def select_icon_prompt(description: str, options: List[str]) -> str:

    prompt = (
        f"""I need you to help me find the right icon to click on a web page. I am going to provide you with {len(options)} images. You can refer to them by their index starting with zero, return -1 if none of the options make sense, 
        so you have the options -1 to {len(options)}. Please select the icon that best matches the description '{description}' by returning the index number as an integer.
        This icon should be something you can click on a web page"""
        + """
Please return the index as a json object

Here is an example:
{
    "reason": "This image matches the description because it is a search bar that you could click on",
    "index": 2
}

And if you didn't want to select any of the options you would return:
{
    "reason": "None of these images match the description"
    "index": -1
}
"""
    )
    content = [
        {
            "type": "text",
            "text": prompt,
        },
    ]
    for i, img in enumerate(options):
        with open(img, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

            print("Adding content: ", img, " at index: ", i)
            img_content = {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{encoded_string}"},
            }
            content.append(img_content)

    msg = {"role": "user", "content": content}
    return msg


def select_icon_prompt_composite(description: str, combined_img_path: str) -> str:

    prompt = (
        f"""I need you to help me find the right icon to click on a web page. I am going to provide you with a composite image that has all of the icon options.
        You can refer to the icon by the index number beside it. Please select the icon that best matches the description '{description}' by returning the index number as an integer.
        This icon should be something you can click on a web page"""
        + """
Please return the index as a json object

Here is an example:
{
    "reason": "This image matches the description because it is a search bar that you could click on",
    "index": 2
}
"""
    )
    content = [
        {
            "type": "text",
            "text": prompt,
        },
    ]

    with open(combined_img_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

        img_content = {
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{encoded_string}"},
        }
        content.append(img_content)

    msg = {"role": "user", "content": content}
    return msg
