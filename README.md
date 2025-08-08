# 🧸 Teddy Bear Detection System 🧸

**Author**: Vishnu AJay  
**Date**: 9/26/2022  
**Project**: Teddy Bear Detection with TensorFlow & OpenCV  


https://youtu.be/FTTMfeGV4JY
---

**"Lights, Camera, Teddy Bear!"**  

This project uses **TensorFlow**, **OpenCV**, and a pre-trained deep learning model to detect a very specific and huggable friend—teddy bears! If a teddy bear is spotted on camera, the system provides audio feedback and starts recording a video. Now, you'll never miss a cuddly moment again! 🧸🎥

---

## 🧸 Project Overview
DOWNLOAD THE TENSOR FLOW MODEL FROM HERE : https://drive.google.com/file/d/1wo24-zq2eomBsVj6q9nIImyymYFpXa71/view?usp=sharing 


This project loads a pre-trained **TensorFlow** object detection model and uses a webcam (or an image) to detect objects, particularly **teddy bears** 🧸. When a teddy bear is detected, the system provides a voice alert using **pyttsx3** (text-to-speech), draws bounding boxes around detected objects, and saves a video recording of the detection event.

## 🛠 Features

- **Real-Time Object Detection**: Detects objects using a **TensorFlow SSD MobileNet** model trained on the **COCO dataset**.
- **Teddy Bear Detection**: Specifically identifies teddy bears and responds with both visual and audio alerts.
- **Automatic Recording**: Records 20 seconds of footage when a teddy bear is detected and saves it to your computer.
- **Audio Alerts**: Uses a text-to-speech engine to announce when a teddy bear is detected. ("Teddy Bear Detected!")
- **Image & Webcam Support**: Can either process a static image or live webcam feed for detection.

---

## ✨ Components & Libraries

1. **TensorFlow**: The neural network used for object detection.
2. **OpenCV**: For capturing images, drawing bounding boxes, and handling webcam/video feed.
3. **pyttsx3**: A text-to-speech engine for audio feedback.
4. **Pickle**: Loads COCO dataset labels for object classification.
5. **Python**: The language powering this magic! 🐍

### 💻 Libraries Required

- `numpy`
- `opencv-python`
- `pyttsx3`
- `pickle`

To install these, run:

```bash
pip install numpy opencv-python pyttsx3
