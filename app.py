import streamlit as st
from tts_main import main as speechify

st.write("## Narrated Books \n Audio books that sound natural")

# file = st.file_uploader("Upload your files here")

text = st.text_area("Input Text Here", height=300)
if st.button("Speechify"):  
    audio_path = "data/output.mp3"
    speechify(text, audio_path)          
    st.audio(audio_path)
