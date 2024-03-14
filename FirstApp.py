import streamlit as st
from PIL import Image

st.title('File Uploading')

st.subheader("1. Uploading an Image")
img_file = st.file_uploader('Upload Image', type = ['png', 'jpeg', 'jpg'])
if img_file is not None:
    
    file_details = {'file_name' : img_file.name, 'file_type' : img_file.type,
                    'file_size' : img_file.size}
    
    st.write(file_details)
    st.image(Image.open(img_file))
    
    
st.subheader("2. Uploading an Audio")
audio_file = st.file_uploader('Upload Audio', type = ['wav', 'mp3'])
if audio_file is not None:
    
    file_details = {'file_name' : audio_file.name, 'file_type' : audio_file.type,
                    'file_size' : audio_file.size}
    
    st.write(file_details)
    st.audio(audio_file)
    
st.subheader("3. Uploading Video")
video_file = st.file_uploader('Upload Video', type = ['mov', 'mp4'])
if video_file is not None:
    
    file_details = {'file_name' : video_file.name, 'file_type' : video_file.type,
                    'file_size' : video_file.size}
    
    st.write(file_details)
    st.video(video_file)
