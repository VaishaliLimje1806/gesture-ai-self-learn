import time
import cv2
import pyautogui
from actions import tab_switch_action, click_action, screenshot_action
from detection import get_hand_landmarks
from gesture_utils import is_pinch, is_swipe, is_hold
from ui_utils import draw_feedback

# Capture frame
cap = cv2.VideoCapture(0)

gesture_feedback = ""
initial_position = None
prev_index_pos = 0,0
already_clicked = False
screen_w, screen_h = pyautogui.size()

start_time = time.time()
click_start_time, feedback_start_time = 0,0
swipe_start_time = 0
swipe_cooldown = 1
pinch_start_time = None
PINCH_HOLD_TIME = 0.3  # seconds

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    results, landmark_list = get_hand_landmarks(frame)

    if landmark_list:

        # if pinch is detected for 0.3 seconds, mouse click will be triggered.
        if is_pinch(landmark_list):
            if not pinch_start_time:
                pinch_start_time = time.time()
            elif time.time() - pinch_start_time >= PINCH_HOLD_TIME and not already_clicked:
                gesture_feedback = "Click"
                feedback_start_time = time.time()
                click_action()
                already_clicked = True
                click_start_time = time.time()
        else:
            pinch_start_time = None

        # if swipe is detected, tab will be moved to that swipe direction in browser.
        swipe_direction = is_swipe(landmark_list, prev_index_pos)
        if swipe_direction and time.time() - swipe_start_time > swipe_cooldown:
            tab_switch_action(swipe_direction)
            gesture_feedback = f"Swipe {swipe_direction.capitalize()}"
            feedback_start_time = time.time()
            swipe_start_time = time.time()
        prev_index_pos = landmark_list[8]
        index_tip = landmark_list[8]

        # If initial_position is not set, or finger moved too much, reset
        distance = ((index_tip[0] - initial_position[0]) ** 2 + (
                    index_tip[1] - initial_position[1]) ** 2) ** 0.5 if initial_position else None
        if initial_position is None or distance > 20:
            initial_position = index_tip
            start_time = time.time()

        # If index finger is hold for 5 seconds, screenshot will be taken.
        if is_hold(landmark_list, initial_position, start_time):
            gesture_feedback = "Screenshot taken"
            feedback_start_time = time.time()
            screenshot_action()
            start_time = time.time()
            initial_position = None

        if time.time() - click_start_time > 1 and already_clicked and not is_pinch(landmark_list):
            already_clicked = False

    if time.time() - feedback_start_time > 1.5:
        gesture_feedback = ""
    draw_feedback(frame, gesture_feedback)
    cv2.imshow('frame:', frame)

    if cv2.waitKey(1) == ord('q'):
        break

# Release the window
print("Exited gesture control app.")
cap.release()
cv2.destroyAllWindows()