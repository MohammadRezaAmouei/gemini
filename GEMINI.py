import google.generativeai as genai
from PIL import Image
import streamlit as st

API = st.text_input("put your api")

genai.configure(api_key=API)

models = st.selectbox("select your model", ["gemini-pro", "gemini-pro-vision"])

model = genai.GenerativeModel(models)

if models == "gemini-pro-vision":
    image_upload = st.file_uploader("upload your image")
    if image_upload:
        img = Image.open(image_upload)
        response = model.generate_content(["Write a prompt for me to create an image like this", img])
        st.write(response.text)
elif models == "gemini-pro":
    inp = st.text_area("write your prompt")
    if inp != "":
        response = model.generate_content(inp)
        st.write(response.text)
