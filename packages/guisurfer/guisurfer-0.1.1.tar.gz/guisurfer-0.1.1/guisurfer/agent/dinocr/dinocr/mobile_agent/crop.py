# Inspired from MobileAgent

import math
import cv2
import numpy as np
from PIL import Image, ImageDraw
from typing import List, Tuple, Optional


def crop_perspective(img: np.array, position: np.array) -> np.array:
    """Crops the image to a new perspective based on given position points.

    Args:
        img: Image array.
        position: Array of position points.

    Returns:
        Cropped image array.
    """

    def euclidean_distance(x1: float, y1: float, x2: float, y2: float) -> float:
        """Calculates the Euclidean distance between two points."""
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    position = position.tolist()
    position.sort(key=lambda x: x[0])
    position[:2] = sorted(position[:2], key=lambda x: x[1])
    position[2:] = sorted(position[2:], key=lambda x: x[1])

    x1, y1, x2, y2, x3, y3, x4, y4 = (
        *position[0],
        *position[2],
        *position[3],
        *position[1],
    )

    corners = np.array([[x1, y1], [x2, y2], [x4, y4], [x3, y3]], np.float32)
    img_width = euclidean_distance(
        (x1 + x4) / 2, (y1 + y4) / 2, (x2 + x3) / 2, (y2 + y3) / 2
    )
    img_height = euclidean_distance(
        (x1 + x2) / 2, (y1 + y2) / 2, (x4 + x3) / 2, (y4 + y3) / 2
    )

    target_corners = np.array(
        [
            [0, 0],
            [img_width - 1, 0],
            [0, img_height - 1],
            [img_width - 1, img_height - 1],
        ],
        np.float32,
    )
    transform = cv2.getPerspectiveTransform(corners, target_corners)
    dst = cv2.warpPerspective(img, transform, (int(img_width), int(img_height)))

    return dst


def box_size(box: Tuple[int, int, int, int]) -> int:
    """Calculates the size of a bounding box.

    Args:
        box: A tuple (x_min, y_min, x_max, y_max) representing the bounding box.

    Returns:
        The area of the bounding box.
    """
    return (box[2] - box[0]) * (box[3] - box[1])


def box_iou(box1: Tuple[int, int, int, int], box2: Tuple[int, int, int, int]) -> float:
    """Calculates the Intersection over Union (IoU) of two bounding boxes.

    Args:
        box1: First bounding box.
        box2: Second bounding box.

    Returns:
        The IoU of the two bounding boxes.
    """
    xA, yA = max(box1[0], box2[0]), max(box1[1], box2[1])
    xB, yB = min(box1[2], box2[2]), min(box1[3], box2[3])

    interArea = max(0, xB - xA) * max(0, yB - yA)
    box1Area, box2Area = box_size(box1), box_size(box2)
    iou = interArea / float(box1Area + box2Area - interArea)

    return iou


def crop_and_save(
    image_path: str,
    box: Tuple[int, int, int, int],
    index: int,
    text_data: Optional[Tuple[int, int, int, int]] = None,
) -> None:
    """Crops an image and optionally draws a rectangle around given text data, then saves the image.

    Args:
        image_path: Path to the image to crop.
        box: Bounding box to crop around.
        index: Index to name the saved file.
        text_data: Optional bounding box for text data to highlight.
    """
    image = Image.open(image_path)

    if text_data:
        draw = ImageDraw.Draw(image)
        draw.rectangle(
            ((text_data[0], text_data[1]), (text_data[2], text_data[3])),
            outline="red",
            width=5,
        )

    cropped_image = image.crop(box)
    print(f"saving img: ./temp/{index}.jpg")
    cropped_image.save(f"./temp/{index}.jpg")


def is_within_box(
    box: Tuple[int, int, int, int], target: Tuple[int, int, int, int]
) -> bool:
    """Checks if a box is entirely within another box.

    Args:
        box: The inner box.
        target: The outer box.

    Returns:
        True if the inner box is entirely within the outer box, else False.
    """
    return all(
        [box[0] > target[0], box[1] > target[1], box[2] < target[2], box[3] < target[3]]
    )


def crop_based_on_position(
    image_path: str, box: Tuple[int, int, int, int], index: int, position: str
) -> bool:
    """Crops the image based on the specified position and saves if within bounds.

    Args:
        image_path: Path to the image to crop.
        box: Bounding box to crop around.
        index: Index for naming the saved file.
        position: The position specifier (e.g., 'left', 'right').

    Returns:
        True if the crop was within the specified position bounds and saved, else False.
    """
    image = Image.open(image_path)
    w, h = image.size
    bounds = {
        "left": [0, 0, w / 2, h],
        "right": [w / 2, 0, w, h],
        "top": [0, 0, w, h / 2],
        "bottom": [0, h / 2, w, h],
        "top left": [0, 0, w / 2, h / 2],
        "top right": [w / 2, 0, w, h / 2],
        "bottom left": [0, h / 2, w / 2, h],
        "bottom right": [w / 2, h / 2, w, h],
    }.get(position, [0, 0, w, h])

    if is_within_box(box, bounds):
        cropped_image = image.crop(box)
        cropped_image.save(f"./temp/{index}.jpg")
        return True
    return False
