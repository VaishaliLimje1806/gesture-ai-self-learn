import pyautogui


def move_cursor(index_finger_pos, screen_size, prev_pos, frame_shape, smoothing_factor=2):
    """
    Moves the mouse pointer to the given screen coordinates.

    Args:
        index_finger_pos (tuple): (x, y) position of index fingertip.
        screen_size (tuple): Size of user’s screen.
    """
    index_finger_x, index_finger_y = index_finger_pos
    screen_width, screen_height = screen_size
    prev_x, prev_y = prev_pos
    h, w, _ = frame_shape
    smooth_x, smooth_y = prev_x, prev_y

    if index_finger_x is not None and index_finger_y is not None:
        target_x_screen = (index_finger_x / w) * screen_width
        target_y_screen = (index_finger_y / h) * screen_height

        smooth_x = (1 - smoothing_factor) * prev_x + smoothing_factor * target_x_screen
        smooth_y = (1 - smoothing_factor) * prev_y + smoothing_factor * target_y_screen

        pyautogui.moveTo(smooth_x, smooth_y)

    return (smooth_x, smooth_y)