"""Real-time hand tracking demo using OpenCV and MediaPipe."""

from __future__ import annotations

import cv2
import mediapipe as mp


def create_hands_tracker() -> mp.solutions.hands.Hands:
    """Create and configure the MediaPipe hand tracker."""
    return mp.solutions.hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5,
    )


def main() -> None:
    """Open the webcam, detect hands, and draw landmarks until the user quits."""
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        raise RuntimeError(
            "Unable to access the webcam. Please connect a camera and try again."
        )

    drawing_utils = mp.solutions.drawing_utils
    hands = create_hands_tracker()

    try:
        while True:
            success, frame = capture.read()
            if not success or frame is None:
                print("Failed to read a frame from the camera.")
                break

            image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
            results = hands.process(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    drawing_utils.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp.solutions.hands.HAND_CONNECTIONS,
                        drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                        drawing_utils.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2),
                    )

            cv2.putText(
                image,
                "Press ESC to quit",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2,
            )
            cv2.imshow("Hand Tracker", image)

            if cv2.waitKey(1) & 0xFF == 27:
                break
    finally:
        capture.release()
        cv2.destroyAllWindows()
        hands.close()


if __name__ == "__main__":
    main()

