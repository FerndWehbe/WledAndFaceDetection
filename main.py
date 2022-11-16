from wled_control import set_bri
import threading
import cv2

face_cascade = cv2.CascadeClassifier(
    r"model\haarcascade_frontalface_default.xml"
)

video_capture = cv2.VideoCapture(0)

video_capture.set(cv2.CAP_PROP_FPS, 30.0)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, int(1920 / 3))
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, int(1080 / 3))

has_people = False
num_peoples = 0


def set_color(has_people, num_peoples, num_faces):
    if num_peoples != num_faces:
        num_peoples = num_faces
        if has_people:
            bri = min(15 * num_faces, 255)
        else:
            bri = 2
        t1 = threading.Thread(target=set_bri, args=(bri,))
        t1.start()
    return num_peoples


while True:
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE,
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    num_faces = len(faces)
    has_people = True if num_faces else False

    num_peoples = set_color(has_people, num_peoples, num_faces)

    cv2.imshow("video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
