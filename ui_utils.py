import cv2

def draw_feedback(frame, text):
    cv2.putText(
        frame,
        text,
        (50, 50),  # position (x, y)
        cv2.FONT_HERSHEY_SIMPLEX,  # font
        1.0,  # font scale
        (0, 255, 0),  # color (green)
        2,  # thickness
        cv2.LINE_AA  # anti-alias
    )
    return