import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 500)
while True:
    succes, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break