# Hand-detection

This project demonstrates real-time hand detection and tracking using MediaPipe’s Hand Landmark Model combined with OpenCV for video capture and visualization.
It accurately detects 21 key hand landmarks, tracks finger movement, and helps build gesture-based applications such as virtual mouse, hand-gesture control, sign language interpretation, and more.

🚀 Features

Real-time hand detection from webcam

Tracks 21 hand landmarks

Identifies multiple hands

Smooth, lightweight, high-performance MediaPipe Hand Tracking

Easy to extend for gesture control, counting fingers, sign recognition etc.

🧠 How It Works
MediaPipe Hands Pipeline:

Palm Detection – Detects presence of a hand.

Hand Landmark Model – Predicts 21 landmark points.

Tracking – Tracks the hand across frames using ML + geometry.

Rendering – OpenCV draws landmarks and connections.

