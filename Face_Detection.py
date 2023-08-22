import av
import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class FaceDetectionProcessor(VideoProcessorBase):
    def __init__(self, draw_color, min_neighbors, scale_factor):
        self.draw_color = draw_color
        self.min_neighbors = min_neighbors
        self.scale_factor = scale_factor
        self.processed_frame = None

    def recv(self, frame):
        # Convert to ndarray
        frame_data = frame.to_ndarray(format="bgr24")

        # Convert RGBA color to BGR
        bgr_color = tuple(int(self.draw_color[i:i+2], 16) for i in (1, 3, 5))[::-1]

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame_data, cv2.COLOR_BGR2GRAY)

        # Detect the faces using the face cascade classifier
        faces = face_cascade.detectMultiScale(gray, scaleFactor=self.scale_factor, minNeighbors=self.min_neighbors)

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame_data, (x, y), (x + w, y + h), bgr_color, 2)
        
        # Create an av.VideoFrame from the modified ndarray
        self.processed_frame = av.VideoFrame.from_ndarray(frame_data, format='bgr24')
        
        return self.processed_frame
    
def app():
    st.title("Face Detection using Viola-Jones Algorithm")
    st.write("Press the button below to start detecting faces from your webcam")
    
    # Instructions
    st.write("1. Click 'Detect Faces' to start detecting faces.")
    st.write("2. Use the color picker to choose the color of rectangles.")
    st.write("3. Adjust 'minNeighbors' and 'scaleFactor' sliders as needed.")
    
    # User interface for adjusting parameters
    draw_color = st.color_picker("Choose Rectangle Color", value="#00FF00")
    min_neighbors = st.slider("minNeighbors", min_value=1, max_value=10, value=5)
    scale_factor = st.slider("scaleFactor", min_value=1.01, max_value=1.5, value=1.3, step=0.01)
    
    # Initialize the webrtc_streamer with the FaceDetectionProcessor class
    webrtc_ctx = webrtc_streamer(
        key="face-detection",
        video_processor_factory=lambda: FaceDetectionProcessor(draw_color, min_neighbors, scale_factor),
        rtc_configuration=RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})
        )

    # Add a "Download Frame" button
    if st.button("Capture Frame"):
        st.image(webrtc_ctx.video_processor.processed_frame.to_ndarray(), channels="BGR")

if __name__ == "__main__":
    app()
