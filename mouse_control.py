import cv2
import mediapipe as mp
import numpy as np
import time
import pyautogui

# Capture frame
cap = cv2.VideoCapture(0)

# Initialize mediapipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_draw = mp.solutions.drawing_utils
INDEX_FINGER_TIP = 8
screen_width, screen_height = pyautogui.size()
prev_x, prev_y = 0,0
smoothing_factor = 5

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    results = hands.process(img_rgb)

    index_tip_x, index_tip_y = 0, 0
    h, w, _ = img.shape
    # Extracting landmarks of hand
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):

                cx, cy = int(lm.x * w), int(lm.y * h)

                # x and y co-ordinates for Index Finger Tip
                if id == INDEX_FINGER_TIP:
                    index_tip_x, index_tip_y = cx, cy

            if index_tip_x and index_tip_y:
                target_x_screen = (index_tip_x / w) * screen_width
                target_y_screen = (index_tip_y / h) * screen_height

                smooth_x = prev_x + (target_x_screen - prev_x)/smoothing_factor
                smooth_y = prev_y + (target_y_screen - prev_y) / smoothing_factor

                pyautogui.moveTo(smooth_x, smooth_y)
                prev_x, prev_y = smooth_x, smooth_y

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
    else:
        print("No hand detected.")

    # Display output
    cv2.imshow('Hand Detection', img)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()