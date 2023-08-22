# Face Detection Web App using Viola-Jones Algorithm

This repository contains a simple web app built using Streamlit for real-time face detection using the Viola-Jones algorithm. The application allows users to detect faces from their webcam feed, draw rectangles around the detected faces, and customize the appearance of the rectangles.

## Description

The main components of the code include:

1. **Importing Libraries:** The necessary libraries, including `av`, `cv2`, and `streamlit`, are imported to enable video processing and building the web app interface.

2. **Face Detection Processor:** A class called `FaceDetectionProcessor` is defined, which inherits from `VideoProcessorBase` provided by the `streamlit_webrtc` library. This class processes video frames, detects faces using the Viola-Jones algorithm, and draws rectangles around the detected faces. The processor also handles the customization of the rectangle color and face detection parameters.

3. **Web App Interface:** The `app` function is defined to build the Streamlit web app interface. Users can adjust the parameters for face detection, such as rectangle color, `minNeighbors`, and `scaleFactor`, using sliders and a color picker. The `webrtc_streamer` function from the `streamlit_webrtc` library is used to initialize the video stream and connect it to the `FaceDetectionProcessor`.

4. **Capturing Frames:** The web app also includes a "Capture Frame" button that allows users to capture a single frame with detected faces and display it in the interface.

## Instructions

1. Click the "Detect Faces" button to start detecting faces from your webcam.
2. Use the color picker to choose the color of the rectangles drawn around the detected faces.
3. Adjust the "minNeighbors" and "scaleFactor" sliders as needed to fine-tune face detection parameters.
4. Press the "Capture Frame" button to capture a frame with detected faces.

## Web App Link

[Access the Face Detection Web App](https://face-detection-eutctgzkvomtptnmnegs2t.streamlit.app/)
