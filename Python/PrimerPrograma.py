import cv2
import pyautogui
from cvzone.HandTrackingModule import HandDetector

video = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.0 ,maxHands=2)

while True:
    ret,marco= video.read()
    hands,img = detector.findHands(marco)
    #print(hands)
    if hands:
        mano= hands[0]
        dedosarriba = detector.fingersUp(mano)
        ##print(dedosarriba)
        if dedosarriba == [0, 0, 0, 0, 0]:
            pyautogui.press("space")
            ##print("Se usa el espacio.")
    cv2.imshow("video", marco)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break