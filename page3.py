# ==================================================
# PAGE 3 : PH DETECTION
# ==================================================
# Import Libraries
import streamlit as st
import numpy as np

# Input Needed Image
from PIL import Image
import requests
from io import BytesIO

url1 = "https://drive.google.com/uc?export=download&id=1Tj0anph6-lVTRn16FVwWivIYU027Tosy"
response1 = requests.get(url1)
logo = Image.open(BytesIO(response1.content))

# Background and Theme Adjustment
st.markdown(
    """
    <style>
    .stApp
    {
        background: linear-gradient(to bottom, #bce8e7, #0ba1a2);
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
tit1, tit2 = st.columns([4, 3])
with tit1:
    st.image(logo)
with tit2:
    st.header("pHocus Smart Patch")
    st.write("### Heal. Track. Predict.")
st.write("""
##### A pH detector to measure your skin pH from just a photo of patch!
""")

# User Input
st.write("### Input Photo")
predict = st.file_uploader("", type=["jpg", "jpeg", "png"])

if predict is not None:
    # Display the uploaded image
    image = Image.open(predict)
    st.image(image, use_container_width=True)

# enter pH detection model

# Prediction Output
st.write("### Prediction Results")
prediction_result = 0.0
d = prediction_result - 5.5
dcolor=""
if d==0:
    dcolor = "off"
elif d<=0:
    dcolor = "normal"
elif d>=0:
    dcolor = "inverse"

# # Load Using Pickle
# import pickle
# with open('model.pkl', 'rb') as f:
#     ph = pickle.load(f)

# # Data Processing
# res = ph.predict(predict)