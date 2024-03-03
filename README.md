#Teddy_Bear_Detector

The core of our device is like a teddy bear detector. Think of it as a 
security camera, but instead of catching burglars, it's on the lookout for teddy 
bears. When it spots one, not only does it recognize it, but it also takes a 
short video of it and shouts out, "Teddy bear detected!" via a speech 
announcement. This is a modification on the exisitng code detect.py.
Raspberry Pi: It runs the main script and manages both the camera and the 
audio output.
Camera: Attached to the Pi, it continuously captures video. With the help of 
the OpenCV library, it processes the video to look for the teddy bear.
Speakers: These are connected to the Pi to play the speech output.
How It Operates:
Once the detect.py is run. The device recognizes the teddy bear, starts 
recording a video clip, and also audibly announces. After recording for 20 
seconds, it saves the video clip to a specific folder.
OpenCV: . Using a trained CV model, our device can detect objects, 
including teddy bears. When it finds one in the camera's view, it draws a box 
around it, labels it and triggers the recording. The code is looking for the 
apprance of the label in this case.
Speech Capabilities: Once a teddy bear is detected, the device uses pyTTS 
to convert the text message "Teddy bear detected!" into speech. This is then 
played out loud, so you know a teddy has been spotted even if you're not 
looking at the screen. It recording in the "Recodings" directory and with 
current time stamp. The writing process uses Gstreamer with a MJPG 
codec. The recorded files are saved as a short AVI file. 
In essence, our device is a fun blend of computer vision and speech capabilities.
