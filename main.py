import cv2
import time


video = cv2.VideoCapture(1)
time.sleep(1)

while True:
    check, frame = video.read()
    cv2.imshow("My Video", frame)
    print(frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()