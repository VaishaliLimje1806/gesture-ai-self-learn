# 🖐️ Gesture-Controlled AI – Self Learning Project

> Real-time gesture control system built with **Python, OpenCV, MediaPipe**, and **pyautogui**  
> _Originally started as a self-learning project by Vaishali Limje — now a functional, feature-rich automation toolkit!_

---

## 🔍 Project Goal

Build a system that detects hand gestures via webcam and maps them to real-world computer actions like:
- Swiping slides
- Taking screenshots
- Switching tabs/windows
- Moving cursor
- **Clicking with pinch gesture**

---

## ✅ Features

- ✅ Real-time hand tracking with MediaPipe
- ✅ Finger gesture detection (UP/DOWN status)
- ✅ Smoothed cursor control via fingertip
- ✅ **Pinch-to-click** mouse simulation
- ✅ Screenshot trigger with gesture-hold
- ✅ Swipe left/right gesture for tab switching
- ✅ Clean modular Python scripts for each phase

---

## 🛠️ Tech Stack

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- Git & GitHub

---

## 🚀 How to Run

```bash
git clone https://github.com/VaishaliLimje1806/gesture-ai-self-learn
cd gesture-ai-self-learn
pip install -r requirements.txt
python main.py

⚠️ Make sure your webcam is enabled, and use the system in good lighting conditions.
```

---
## 📁 Project Phases

| Phase    | Task Description                                         | File(s)              |
|----------|----------------------------------------------------------|----------------------|
| Phase 1  | Open webcam and display layout                           | `main.py`            |
| Phase 2  | Hand detection with MediaPipe                            | `detection.py`       |
| Phase 3  | Finger gesture logic (pinch, swipe, hold)                | `gesture_utils.py`   |
| Phase 4  | Gesture-triggered actions (click, screenshot, tab switch)| `gesture_actions.py` |
| Phase 5  | Smoothed cursor control via fingertip                   | `mouse_control.py`   |
| Phase 6  | On-screen gesture feedback overlay                       | `ui_utils.py`        |
| Phase 7  | Final integration of all modules                         | `main.py`            |

---

## 📚 Author's Note

> This was a self-driven AI mini-project to break into real-time automation using vision.
I used no pre-built code or tutorials — just documentation, reasoning, and trial & error.
It helped me master OpenCV, gesture-based UX, real-time event detection, and modular Python design.

---

## 🌟 Future Enhancements

- Scroll gesture simulation  
- Gesture-based drag and drop  
- Volume control  
- Integration with browser or media apps  
- Voice feedback using TTS

---

## 👩‍💻 Author

**Vaishali Limje**  
[GitHub Profile](https://github.com/VaishaliLimje1806)

