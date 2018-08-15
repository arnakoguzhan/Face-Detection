import cv2
import imageio

face_cascade = cv2.CascadeClassifier("models/haarcascade-frontalface-default.xml")
eye_cascade = cv2.CascadeClassifier("models/haarcascade-eye.xml")

def detect(frame):
    # convert video color to black&white
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detect faces on video
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    # Draw a frame around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        gray_face = gray[y:y + h, x:x + w]
        color_face = frame[y:y + h, x:x + w]
        # Detect eyes on face
        eyes = eye_cascade.detectMultiScale(gray_face, 1.1, 3)
        # Draw a frame around each eye
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(color_face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    return frame

reader = imageio.get_reader('input-video.mp4')
FPS = reader.get_meta_data()['fps']
writer = imageio.get_writer('output-video.mp4', fps=FPS)

for i, frame in enumerate(reader):
    frame = detect(frame)
    writer.append_data(frame)
    print(i)
writer.close()
