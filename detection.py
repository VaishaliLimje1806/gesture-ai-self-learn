import mediapipe as mp
import cv2

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

def get_hand_landmarks(frame):
    """
    Detects hand landmarks from a given video frame using MediaPipe.

    Args:
        frame (np.ndarray): BGR image from OpenCV.

    Returns:
        results (object): MediaPipe detection results.
        landmarks_list (list): List of (x, y) tuples for key landmarks.
    """
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    landmarks_list = []

    # Extracting landmarks of hand
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                x = int(lm.x * frame.shape[1])
                y = int(lm.y * frame.shape[0])
                landmarks_list.append((x,y))

        mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

    return results, landmarks_list