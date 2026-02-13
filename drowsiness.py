import cv2
import time
import winsound  # Windows only

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

face_not_found_start = None
alert_triggered = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    if len(faces) == 0:
        if face_not_found_start is None:
            face_not_found_start = time.time()
        else:
            elapsed = time.time() - face_not_found_start
            if elapsed >= 5 and not alert_triggered:
                print("?? Drowsiness Alert! No face detected.")
                winsound.Beep(1000, 700)
                alert_triggered = True
    else:
        face_not_found_start = None
        alert_triggered = False

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    status = "Face Detected" if len(faces) > 0 else "No Face Detected"
    color = (0, 255, 0) if len(faces) > 0 else (0, 0, 255)

    cv2.putText(frame, status, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("Driver Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
