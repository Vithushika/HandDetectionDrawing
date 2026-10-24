# HandDetectionDrawing
A Python computer vision project that uses a webcam to track a hand in real time and create 
drawings by following the index fingertip. Built with OpenCV and MediaPipe, the application 
overlays hand landmarks and connections on the camera feed and provides keyboard controls 
for drawing mode, brush size, colour and clearing the canvas.

## Features
- **Real-time hand tracking** using MediaPipe Hand Landmarker.
- **Hand landmark visualization** with connections between selected landmarks.
- **Fingertip-based drawing** using the index fingertip as the cursor.
- **Toggle drawing mode** on and off with the spacebar.
- **Adjustable brush size** using the `=` and `-` keys.
- **Clear the canvas** with the `C` key.
- **Live status display** showing drawing mode and the selected brush size.
- **Webcam input** processed frame by frame using OpenCV.

## Technologies
- Python
- OpenCV (`opencv-python`)
- MediaPipe

## Requirements
- Python 3.9 or another Python version supported by your installed MediaPipe release
- A webcam
- The MediaPipe Hand Landmarker model file: `hand_landmarker.task` located in the working directory

Download the **Hand Landmarker model** from the official MediaPipe documentation and place the file in the project folder:
https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker

## Controls
- `c` - clears the canvas of all drawings
- `-` - decreases brush size
- `=` - increases brush size
- `esc` - exit the application
- `space` - toggle drawing mode on and off




