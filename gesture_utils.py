import math
import time

import pyautogui


def is_pinch(landmarks, threshold=40):
    """
    Checks if thumb and index finger are pinched.

    Args:
        landmarks (list): List of (x, y) landmark positions.
        threshold (float): Pixel distance to count as pinch.

    Returns:
        bool: True if pinch is detected.
    """
    if len(landmarks) < 8:
        return False

    THUMB_TIP_ID = 4
    INDEX_FINDER_TIP = 8

    thumb_x, thumb_y = landmarks[THUMB_TIP_ID]
    index_x, index_y = landmarks[INDEX_FINDER_TIP]

    if thumb_x is not None and index_x is not None:
        distance = math.sqrt((thumb_x - index_x)**2 + (thumb_y - index_y)**2)
        if distance < threshold:
            # print("Pinch detected")
            return True
    return False

def is_swipe(landmarks, prev_position):
    """
    Detects left or right swipe based on movement pattern.

    Returns:
        str: 'left', 'right', or None
    """
    INDEX_FINGER_TIP = 8
    curr_index_x, _ = landmarks[INDEX_FINGER_TIP]
    prev_index_x, _ = prev_position
    delta = curr_index_x - prev_index_x

    if delta > 50:
        return 'right'
    elif delta < -50:
        return 'left'
    return None

def is_hold(landmarks, initial_position, start_time, hold_time=5.0):
    """
    Checks if a finger is held up for a continuous duration.

    Returns:
        bool: True if held gesture is detected.
    """
    if initial_position is None:
        return False
    curr_x, curr_y = landmarks[8]
    distance = math.sqrt((curr_x - initial_position[0]) ** 2 + (curr_y - initial_position[1]) ** 2)
    return distance < 20 and (time.time() - start_time) > hold_time
