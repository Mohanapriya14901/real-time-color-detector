import cv2
import numpy as np

# Global variables
clicked = False
r = g = b = xpos = ypos = 0

# Mouse callback function
def get_color(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        xpos = x
        ypos = y

        # Get BGR values at clicked pixel
        b, g, r = frame[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

# Create window and attach mouse callback
cv2.namedWindow("Real-Time Color Detector")
cv2.setMouseCallback("Real-Time Color Detector", get_color)

# Start webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if clicked:
        # Draw color rectangle
        cv2.rectangle(frame, (20, 20), (600, 80), (b, g, r), -1)

        # Display RGB values
        text = f"R = {r}  G = {g}  B = {b}"

        # Use inverted color for better visibility
        cv2.putText(frame, text, (30, 65),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255 - r, 255 - g, 255 - b),
                    2)

    cv2.imshow("Real-Time Color Detector", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
