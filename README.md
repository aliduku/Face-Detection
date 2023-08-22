# Face Detection using Viola-Jones Algorithm

This is a simple Python script that utilizes the Viola-Jones algorithm to detect faces from a webcam stream. The detected faces are outlined with rectangles and can be adjusted in terms of color, detection sensitivity, and other parameters.

## Overview

This script uses the OpenCV library for face detection and Streamlit for the graphical user interface. It allows users to adjust the parameters for face detection, such as the color of the rectangles, the `minNeighbors` parameter, and the `scaleFactor` parameter. Detected faces are outlined with rectangles, and the processed frames can also be saved as an image.

## Description

The script consists of the following main components:

1. **Face Detection Function**: The `detect_faces` function takes the user-defined parameters, initializes the webcam, and processes the video stream to detect faces. It converts the RGBA color chosen by the user into the BGR format suitable for OpenCV. Detected faces are outlined with rectangles using the specified color. If faces are detected, the processed frame is saved as an image named "detected_faces.jpg."

2. **Streamlit App Function**: The `app` function creates the Streamlit web app interface. It provides instructions for using the app, including starting the face detection process, choosing rectangle colors, adjusting parameters, and stopping the detection. Users can interact with sliders and a color picker to adjust the parameters. When the "Detect Faces" button is clicked, the `detect_faces` function is called with the selected parameters.

3. **Main Execution**: The script's execution starts with the `__name__ == "__main__"` block, which calls the `app` function to launch the Streamlit web app.

## Web App

You can interact with the face detection application by clicking [here](https://placeholder-link-to-streamlit-app).

---

Feel free to explore the code and run the application to see the Viola-Jones face detection algorithm in action.
