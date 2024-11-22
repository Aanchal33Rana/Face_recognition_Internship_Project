import cv2

# Test if OpenCV is working
print(cv2.__version__)

# Test VideoCapture
video_capture = cv2.VideoCapture(0)
if video_capture.isOpened():
    print("Camera opened successfully.")
else:
    print("Failed to open the camera.")
video_capture.release()
