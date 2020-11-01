import cv2

# Image File
img_file = "cars_on_highway.jpg"
# video = cv2.VideoCapture("tesla.mp4")
video = cv2.VideoCapture("motorbike.mp4")

# our Pre-trained Car Classifier Code is Below
classifier_file = "car_detector.xml"
pedestrian_file = "pedestrian_detector.xml"

# Create a Car Classifier 
car_tracker = cv2.CascadeClassifier(classifier_file)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_file)

# Run Forever until the car stops
while True:
    (read_successful, frame) = video.read()

    if read_successful:
        grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # Detect Cars and Pedestrians
    cars = car_tracker.detectMultiScale(grayscale_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscale_frame)

    # print(cars)

    # Draw Rectangles Around the cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Draw Rectangles Around the cars
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 225, 255), 2)

    # Display the Image
    cv2.imshow("Car Detector", frame)
    # cv2.imshow("Car Detector", old_image)

    # Don't Close the window automatically
    key = cv2.waitKey(1)

    # Stop if Q key is pressed
    if key == 81 or key == 113:
        break

video.release()


# # create opencv Image
# img = cv2.imread(img_file)
#
# # Create a Car Classifier
# car_tracker = cv2.CascadeClassifier(classifier_file)
#
# # Convert to greyscale image
# old_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # Detect Cars
# cars = car_tracker.detectMultiScale(old_image)
#
# # print(cars)
#
# # Draw Rectangles Around the cars
# for (x, y, w, h) in cars:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
#
# # Display the Image
# cv2.imshow("Car Detector", img)
# # cv2.imshow("Car Detector", old_image)
#
#
# # Don't Close the window automatically
# cv2.waitKey()

