import cv2
import numpy as np
from picamera2 import Picamera2

# Initialisiere die Kamera
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": "RGB888", "size": (640, 480)}))
picam2.start()

# Wartezeit für die Kamera
import time
time.sleep(2)

# Trackbar-Funktion für interaktive Anpassung
def nothing(x):
    pass

# Erstelle ein Fenster und Trackbars für HSV-Werte
cv2.namedWindow("Trackbars")
cv2.createTrackbar("Lower H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("Lower S", "Trackbars", 100, 255, nothing)
cv2.createTrackbar("Lower V", "Trackbars", 50, 255, nothing)
cv2.createTrackbar("Upper H", "Trackbars", 25, 179, nothing)
cv2.createTrackbar("Upper S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("Upper V", "Trackbars", 255, 255, nothing)

# Starte den Stream
while True:
    frame = picam2.capture_array()
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

    # Werte von den Trackbars holen
    lh = cv2.getTrackbarPos("Lower H", "Trackbars")
    ls = cv2.getTrackbarPos("Lower S", "Trackbars")
    lv = cv2.getTrackbarPos("Lower V", "Trackbars")
    uh = cv2.getTrackbarPos("Upper H", "Trackbars")
    us = cv2.getTrackbarPos("Upper S", "Trackbars")
    uv = cv2.getTrackbarPos("Upper V", "Trackbars")

    lower_bound = np.array([lh, ls, lv])
    upper_bound = np.array([uh, us, uv])

    # Maske erstellen und anwenden
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Zeige das Bild und die Maske
    cv2.imshow("Original", frame)
    cv2.imshow("Gefiltert", result)

    # Beenden mit 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
picam2.stop()
