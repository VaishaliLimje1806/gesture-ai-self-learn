import os
import time
import pyautogui

def click_action():
    """Simulates a mouse click."""
    pyautogui.click()
    print("Pinch detected.")
    return True

def screenshot_action():
    """Takes a screenshot and saves it with a timestamp."""
    os.makedirs("screenshots", exist_ok=True)
    ss = pyautogui.screenshot()
    timestamp = int(time.time())
    ss.save(f"screenshots/screenshot_{timestamp}.jpg")
    print("Screenshot taken.")
    return True

def tab_switch_action(direction):
    """
    Switches browser/application tab left or right.

    Args:
        direction (str): 'left' or 'right'
    """
    if direction == 'left':
        pyautogui.hotkey('ctrl', 'shift', 'tab')
        print("Switched tab left")
    elif direction == 'right':
        pyautogui.hotkey('ctrl', 'tab')
        print("Switched tab right")
    return True