import cv2

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FPS, 30.0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, int(1920 / 3))
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, int(1080 / 3))

while 1:
    ret, frame = camera.read()

    cv2.imshow("video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
