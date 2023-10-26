import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Draw blue lines that cross at center of screen
    cv2.line(frame, (int(width/2),0), (int(width/2), height), (255, 0, 0), 1)
    cv2.line(frame, (0,int(height/2)), (width, int(height/2)), (255, 0, 0), 1)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()