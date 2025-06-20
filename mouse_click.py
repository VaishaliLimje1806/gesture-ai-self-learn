import math
import time
import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

THUMB_TIP_ID, INDEX_FINDER_TIP = 4, 8
threshold = 40
already_clicked = False
prev_time = 0

while True:

    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    img_h, img_w, _ = img.shape

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            thumb_x, thumb_y, index_x, index_y = 0, 0, 0, 0
            for id, lm in enumerate(handLms.landmark):

                if id == THUMB_TIP_ID:
                    thumb_x, thumb_y = lm.x*img_w, lm.y*img_h
                elif id == INDEX_FINDER_TIP:
                    index_x, index_y = lm.x*img_w, lm.y*img_h

            if thumb_x is not None and index_x is not None:
                distance = math.sqrt((thumb_x - index_x)**2 + (thumb_y - index_y)**2)

                if distance < threshold and not already_clicked:
                    pyautogui.click()
                    already_clicked = True
                    prev_time = time.time()

                elif distance > threshold and time.time()-prev_time > 0.5:
                    already_clicked = False

                cv2.circle(img, (int(thumb_x), int(thumb_y)), 5, (0, 255, 255), 2)
                cv2.circle(img, (int(index_x), int(index_y)), 5, (255, 255, 0), 2)
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
    else:
        print("No hand detected.")

    cv2.imshow("Hand:", img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()