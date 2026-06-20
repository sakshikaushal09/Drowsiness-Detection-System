import cv2
import mediapipe as mp
import numpy as np
import time

mp_face_mesh = mp.solutions.face_mesh

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

def calculate_ear(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C)

cap = cv2.VideoCapture(0)

EAR_THRESHOLD = 0.22
DROWSY_TIME = 2

start_time = None

with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:

    while True:
        success, frame = cap.read()
        if not success:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb)

        if result.multi_face_landmarks:
            for face_landmarks in result.multi_face_landmarks:

                h, w, _ = frame.shape

                left_eye = np.array([
                    [int(face_landmarks.landmark[p].x * w),
                     int(face_landmarks.landmark[p].y * h)]
                    for p in LEFT_EYE
                ])

                right_eye = np.array([
                    [int(face_landmarks.landmark[p].x * w),
                     int(face_landmarks.landmark[p].y * h)]
                    for p in RIGHT_EYE
                ])

                left_ear = calculate_ear(left_eye)
                right_ear = calculate_ear(right_eye)

                ear = (left_ear + right_ear) / 2

                if ear < EAR_THRESHOLD:
                    if start_time is None:
                        start_time = time.time()

                    if time.time() - start_time > DROWSY_TIME:
                        cv2.putText(
                            frame,
                            "DROWSINESS ALERT!",
                            (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 0, 255),
                            3
                        )
                else:
                    start_time = None

                cv2.putText(
                    frame,
                    f"EAR: {ear:.2f}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 0, 0),
                    2
                )

        cv2.imshow("Drowsiness Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()