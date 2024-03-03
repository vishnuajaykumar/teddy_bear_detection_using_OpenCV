import numpy as np
import cv2
import sys
import pickle
import os
import time
from datetime import datetime
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Load Tensorflow model with OpenCV
tensorflowNet = cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

with open('coco_labels.pickle', 'rb') as handle:
    NameDictionary = pickle.load(handle)

def say(message):
    engine.say(message)
    engine.runAndWait()

img = None
webCam = False

if len(sys.argv) > 1 and not sys.argv[-1] == "noWindow":
    try:
        print("I'll try to read your image")
        img = cv2.imread(sys.argv[1])
        if img is None:
            print("Failed to load image file:", sys.argv[1])
    except:
        print("Failed to load the image are you sure that:", sys.argv[1], "is a path to an image?")
else:
    try:
        print("Trying to open the Webcam.")
        cap = cv2.VideoCapture(0)
        if cap is None or not cap.isOpened():
            raise Exception("No camera")
        webCam = True
    except:
        img = cv2.imread("../data/test.jpg")
        print("Using default image.")

# Setting up directory to save recordings
save_dir = os.path.join(os.path.expanduser("~"), 'Recordings')
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

recording = False
out = None

while True:
    if webCam:
        ret, img = cap.read()

    rows, cols, channels = img.shape

    # Set input for Tensorflow net
    tensorflowNet.setInput(cv2.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))

    # Run a forward pass to compute the net output
    networkOutput = tensorflowNet.forward()

    teddy_bear_detected = False
    for detection in networkOutput[0, 0]:
        score = float(detection[2])
        if score > 0.3:
            classId = int(detection[1])
            label = NameDictionary.get(classId, "")
            if "teddy" in label.lower() and "bear" in label.lower():
                teddy_bear_detected = True
                
            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows

            cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (0, 0, 255), thickness=2)
            cv2.putText(img, label, (int(left), int(top)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    if teddy_bear_detected:
        print("Teddy bear detected!")
        say("Teddy bear detected!")
        if not recording:
            start_time = time.time()
            current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            video_filename = f"teddy_bear_detection_{current_time}.avi"
            video_path = os.path.join(save_dir, video_filename)
            
            fourcc = cv2.VideoWriter_fourcc(*'MJPG')
            out = cv2.VideoWriter(video_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
            recording = True

    if recording:
        out.write(img)
        if time.time() - start_time > 20:  # recording for 20 seconds
            recording = False
            out.release()
            print("Recording saved!")

    if webCam:
        cv2.imshow('detected (press q to quit)', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            if recording:
                out.release()
            cap.release()
            cv2.destroyAllWindows()
            break
