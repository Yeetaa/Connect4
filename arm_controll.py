import cv2
import numpy as np
from picamera2 import Picamera2

#Initialisiere die Kamera
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={'size': (640, 480)}))
picam2.start()

#Wartezeit für die Kamera
import time
time.sleep(2)

#Definiere die Farbe, die herausgefiltert werden soll (Blau)
lower_bound = np.array([100, 150, 50])  # Untere HSV-Grenze
upper_bound = np.array([140, 255, 255])  # Obere HSV-Grenze

#Start Stream
while True:
    frame = picam2.capture_array()
    
    #Konvertiere das Bild in den HSV-Farbraum
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    
    #Erstelle eine Maske 
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    #Wende die Maske auf das Bild an
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    #Zeigt Bilder
    cv2.imshow("Original", frame)
    cv2.imshow("Maske", result)
    
    #Endbedingung
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Muss so
cv2.destroyAllWindows()
picam2.stop()
