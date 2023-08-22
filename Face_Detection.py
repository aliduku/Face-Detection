import cv2
import streamlit as st

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect_faces(draw_color, min_neighbors, scale_factor):
    # Convert RGBA color to BGR
    bgr_color = tuple(int(draw_color[i:i+2], 16) for i in (1, 3, 5))[::-1]

    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    
    # Frame placeholder
    frame_placeholder = st.empty()

    # Add a "Stop" button and store its state in a variable
    stop_button_pressed = st.button("Stop")

    while True:
        # Read the frames from the webcam
        ret, frame = cap.read()

        if not ret:
            st.write("The video capture has ended.")
            break

        # Convert the frames to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect the faces using the face cascade classifier
        faces = face_cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors)
        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), bgr_color, 2)
            # Save the frame with detected faces
            cv2.imwrite("detected_faces.jpg", frame)
        
        # Display the frame using Streamlit's st.image
        frame_placeholder.image(frame, channels="RGB")
        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q') or stop_button_pressed:
            break
    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

def app():
    st.title("Face Detection using Viola-Jones Algorithm")
    st.write("Press the button below to start detecting faces from your webcam")
    
    # Instructions
    st.write("1. Click 'Detect Faces' to start detecting faces.")
    st.write("2. Use the color picker to choose the color of rectangles.")
    st.write("3. Adjust 'minNeighbors' and 'scaleFactor' sliders as needed.")
    st.write("4. Press 'q' to stop the detection.")
    
    # User interface for adjusting parameters
    draw_color = st.color_picker("Choose Rectangle Color", value="#00FF00")
    min_neighbors = st.slider("minNeighbors", min_value=1, max_value=10, value=5)
    scale_factor = st.slider("scaleFactor", min_value=1.01, max_value=1.5, value=1.3, step=0.01)

    # Add a button to start detecting faces
    if st.button("Detect Faces"):       
        # Call the detect_faces function with user-specified parameters
        detect_faces(draw_color, min_neighbors, scale_factor)

if __name__ == "__main__":
    app()
