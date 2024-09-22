import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)  # Use 0 for the built-in camera, or change to 1 for an external camera if needed


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects, _ = hog.detectMultiScale(gray)

    cv2.imshow('Live View', frame)  # Display live camera feed

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
