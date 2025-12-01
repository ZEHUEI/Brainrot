# BrainRot

Lightweight computer-vision demo using **MediaPipe** and **OpenCV** (cv2).  
This repo demonstrates real-time detection / tracking pipelines (e.g. face/pose/hands) and simple visual output. Built in Python and intended for experimentation and learning.

---

## Features

- Real-time webcam capture and visualization with OpenCV.
- MediaPipe pipeline(s) for one or more tasks (face mesh, pose, hands, holistic, etc.).
- Option to process saved video files.
- Optional image save / screenshot support (images/ folder included).

---

## Requirements

- Python 3.8+ (3.10/3.11 recommended)
- `pip` (or use a virtualenv)
- Packages:
  - `opencv-python`
  - `mediapipe` (or `mediapipe-solution` depending on platform)
  - `numpy`
