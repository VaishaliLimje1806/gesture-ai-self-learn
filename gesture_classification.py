import cv2
import mediapipe as mp
import numpy as np

# Capture frame
cap = cv2.VideoCapture(0)

# Initialize mediapipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_draw = mp.solutions.drawing_utils
INDEX_FINGER_TIP = 8
INDEX_FINGER_BASE = 6
prev_stat = ""

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    results = hands.process(img_rgb)

    index_tip_x, index_tip_y, index_base_x, index_base_y = 0, 0, 0, 0

    # Extracting landmarks of hand
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                # x and y co-ordinates for Index Finger Tip and Base
                if id == INDEX_FINGER_TIP:
                    index_tip_x, index_tip_y = cx, cy
                elif id == INDEX_FINGER_BASE:
                    index_base_x, index_base_y = cx, cy

                # If y coordinate of index base is higher than base then Up else DOWN because y-axis increases downwards.
                if index_base_y and index_tip_y:
                    if index_base_y > index_tip_y and prev_stat != "UP":
                        print("Index Finger is UP.")
                        prev_stat = "UP"
                    elif index_base_y < index_tip_y and prev_stat != "DOWN":
                        print("Index Finger is DOWN.")
                        prev_stat = "DOWN"

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
    else:
        print("No hand detected.")

    # Display output
    cv2.putText(img, f"Gesture: {prev_stat}", (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    cv2.imshow('Hand Detection', img)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()