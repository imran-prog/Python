# Importing require modules
import cv2
from random import randrange

# load pre-trained data
# face_tracker = cv2.CascadeClassifier("face_detector.xml")
face_tracker2 = cv2.CascadeClassifier("face_detector2.xml")

# Reading images
# img = cv2.imread("chris-pratt.jpg")
# img = cv2.imread("RDJ.jpg")
img = cv2.imread("crowd2.jpg")
# img = cv2.imread("chris-pratt2.jpg")
# img = cv2.imread("group.JPG")

# Reading video
# video = cv2.VideoCapture(0)
# video = cv2.VideoCapture("walk.mp4")
'''
# Below code is for videos
while True:

    # Reading the current frame
    successful_frame, frame = video.read()

    # Changing the color of the video
    black_n_white = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    # face_detector = face_tracker.detectMultiScale(black_n_white)
    face_detector2 = face_tracker2.detectMultiScale(black_n_white)

    # Making Rectangles Around the Face
    # for (x, y, w, h) in face_detector:
    #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    for (x, y, w, h) in face_detector2:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    #Display the Video
    cv2.imshow("Face Detection System", frame)

    # Don't Quit Automatically
    key = cv2.waitKey(1)

    # Quit the frame with q key
    if key == 81 or key == 113:
        break

video.release()
'''
# Below Code is For Images

# Changing the color of the photo
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_detector = face_tracker2.detectMultiScale(black_n_white)
print(f"These are all the coordinates where the face is located:\n{face_detector}")

# Making Rectangles Around the Face
for (x, y, w, h) in face_detector:
    # cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image
cv2.imshow("Face Detection System", img)

# Don't close automatically
cv2.waitKey()


# Just to check Statement
print("Code Completed")
