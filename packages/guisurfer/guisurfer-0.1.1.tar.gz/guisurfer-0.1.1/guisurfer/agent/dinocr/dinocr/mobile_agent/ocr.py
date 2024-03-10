# Inspired from MobileAgent

import cv2
import numpy as np
from PIL import Image
import logging
from typing import List, Tuple, Any

from .crop import crop_and_save, box_size


def arrange_points(coordinates: List[Tuple[int, int]]) -> np.array:
    """Arranges points in a consistent order based on their angles relative to the centroid.

    Args:
        coordinates: A list of tuples representing points.

    Returns:
        A numpy array of points arranged in order.
    """
    points_array = np.array(coordinates).reshape([4, 2])
    centroid = np.mean(points_array, axis=0)
    angles = np.arctan2(
        points_array[:, 1] - centroid[1], points_array[:, 0] - centroid[0]
    )
    arranged_points = points_array[np.argsort(angles)].astype("float32")

    if arranged_points[0][0] > centroid[0]:
        arranged_points = np.concatenate([arranged_points[3:], arranged_points[:3]])

    return arranged_points


def calculate_lcs_length(string1: str, string2: str) -> int:
    """Computes the length of the longest common substring between two strings.

    Args:
        string1: First string.
        string2: Second string.

    Returns:
        Length of the longest common substring.
    """
    m, n = len(string1), len(string2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def perform_ocr(
    image_path: str,
    prompt: str,
    ocr_detection: Any,
    ocr_recognition: Any,
    target_width: int,
    target_height: int,
) -> Tuple[List[List[int]], List[List[int]]]:
    """Performs OCR on an image, crops images based on detected text, and filters based on a prompt.

    Args:
        image_path: Path to the image.
        prompt: Text prompt to match.
        ocr_detection: OCR detection model or function.
        ocr_recognition: OCR recognition model or function.
        target_width: Target image width for scaling.
        target_height: Target image height for scaling.

    Returns:
        A tuple containing lists of text data and coordinates.
    """
    text_data = []
    coordinates = []
    image = Image.open(image_path)
    image_width, image_height = image.size

    image_cv = cv2.imread(image_path)
    detection_result = ocr_detection(image_cv)["polygons"]
    logging.debug("OCR detection result polys: ", detection_result)

    for i, polygon in enumerate(detection_result):
        ordered_points = arrange_points(polygon)
        cropped_image = crop_and_save(image_cv, ordered_points)
        save_path = f"./temp/cropped_image{i}.jpg"
        cv2.imwrite(save_path, cropped_image)

        recognition_result = ocr_recognition(cropped_image)["text"][0]
        logging.debug("Individual poly OCR result: ", recognition_result)

        if recognition_result == prompt:
            box = [int(e) for e in list(ordered_points.reshape(-1))]
            box = [box[0], box[1], box[4], box[5]]

            if box_size(box) > 0.05 * image_width * image_height:
                continue

            text_data.append(
                [
                    int(max(0, box[0] - 10) * target_width / image_width),
                    int(max(0, box[1] - 10) * target_height / image_height),
                    int(min(box[2] + 10, image_width) * target_width / image_width),
                    int(min(box[3] + 10, image_height) * target_height / image_height),
                ]
            )

            coordinates.append(
                [
                    int(max(0, box[0] - 300) * target_width / image_width),
                    int(max(0, box[1] - 400) * target_height / image_height),
                    int(min(box[2] + 300, image_width) * target_width / image_width),
                    int(min(box[3] + 400, image_height) * target_height / image_height),
                ]
            )

    max_length = 0
    if not text_data:
        for i, polygon in enumerate(detection_result):
            ordered_points = arrange_points(polygon)
            cropped_image = crop_and_save(image_cv, ordered_points)
            save_path = f"./temp/cropped_image_no_match{i}.jpg"
            cv2.imwrite(save_path, cropped_image)

            recognition_result = ocr_recognition(cropped_image)["text"][0]
            logging.debug("OCR no match result: ", recognition_result)

            if len(recognition_result) < 0.3 * len(prompt):
                continue

            now_length = (
                len(recognition_result)
                if recognition_result in prompt
                else calculate_lcs_length(recognition_result, prompt)
            )

            if now_length > max_length:
                max_length = now_length
                box = [int(e) for e in list(ordered_points.reshape(-1))]
                box = [box[0], box[1], box[4], box[5]]

                text_data = [
                    [
                        int(max(0, box[0] - 10) * target_width / image_width),
                        int(max(0, box[1] - 10) * target_height / image_height),
                        int(min(box[2] + 10, image_width) * target_width / image_width),
                        int(
                            min(box[3] + 10, image_height)
                            * target_height
                            / image_height
                        ),
                    ]
                ]

                coordinates = [
                    [
                        int(max(0, box[0] - 300) * target_width / image_width),
                        int(max(0, box[1] - 400) * target_height / image_height),
                        int(
                            min(box[2] + 300, image_width) * target_width / image_width
                        ),
                        int(
                            min(box[3] + 400, image_height)
                            * target_height
                            / image_height
                        ),
                    ]
                ]

        prompt_length_rules = [(10, 0.8), (20, 0.5), (float("inf"), 0.4)]
        for length, threshold in prompt_length_rules:
            if len(prompt) <= length:
                if max_length >= threshold * len(prompt):
                    return text_data, coordinates
                else:
                    return [], []

    return text_data, coordinates
