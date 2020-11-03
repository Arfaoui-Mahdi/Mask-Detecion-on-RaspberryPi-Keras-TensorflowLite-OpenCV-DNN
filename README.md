# Mask-Detecion-on-RaspberryPi-Keras-TensorflowLite-OpenCV-DNN


IN THIS PROJECT, we have used a RASPBERRY PI 3 (B+) with a camera to DETECT Mask on faces.<br>
The sequence is pretty Simple, it is constitued of 3 phases: 

<h1>1/ Face Detection :</h1><br>
The input from camera passed by OpenCV DNN to extract ROI where the face exist.
<br><br>
<h1>2/ Mask Detection :</h1><br>
The ROI pass then through a Tensorflow2.0Lite model to detect if a mask on or off.
<br><br>
<h1>3/ Plotting Results :</h1><br>
taking the given informations, we draw a rectangle either indicating a mask on or off with a confidence percentage.
<br><br><br><br>

<h1>CND Lines :</h1><br>
- Python3 detect_mask_image.py --image your_image_path ==> to detect an input image
<br>
- Python detect_mask_video.py ==> to detect from picamera input

<br><br><br><br><br><br><br><br>

PS : you could see my other repository "Mask Detection Keras Tensorflow2.0 OpenCV DNN" for the PC Version

