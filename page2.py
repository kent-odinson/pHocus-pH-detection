# ==================================================
# PAGE 2 : HOW DOES IT WORK
# ==================================================
# Import Libraries
import streamlit as st
import numpy as np

# Input Needed Image
from PIL import Image
import requests
from io import BytesIO

logo = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1EuzviqgyPz8Ve-jUqounzMGFLfBKKAQz").content))
step = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=18SsN38N21BFjnrfMErqGWRNoaKXtPuQU").content))
wound = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1Y3j_AtiWQFuWujveMVO0n4z1AmUfWAVW").content))
apply = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1kzQDZosjBpGLj0_RC4oZKWF8j76f4CXJ").content))
reaction = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1BJ74UK_dhMn8pyQt5dVr91N-V2Kf9Pfi").content))
capture = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=16Y-kVsYJ1om3-CY9tvu_PBFMpYksp9Aj").content))
predict = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=17Amt6DA4yBw1_bgrRBAczTaL8SO8dObC").content))

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
tit1, tit2 = st.columns([1,3])
with tit1:
    st.image(logo, width=300)
with tit2:
    st.write("## PHocus Smart Patch")
st.write("""
##### A pH detector to measure your skin pH from just a photo of patch!
""")

# How It Works
st.write("""
### How To Use Our Product?
You've got a patch, and your phone. But what to do with them? Here's some explanation to visualize it:
""")
step1, step2 = st.columns([1,3])
with step1:
    st.image(wound, width=500)
    st.image(apply, width=500)
    st.image(reaction, width=500)
    st.image(capture, width=500)
    st.image(predict, width=500)
with step2:
    st.write("""
             #### Ouch!
             Your skin is damaged! Quick treat it as soon as possible!""")
    st.write("")
    st.write("""
             #### Apply!
             Place the pHocus Smartpatch securely on the wound""")
    st.write("")
    st.write("""
             #### React!
             Allow the patch to change color based on the wound's pH level""")
    st.write("")
    st.write("""
             #### Capture!
             After the reaction occur, place the patch in the light box and capture it!""")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("""
             #### Predict!
             Upload the picture to our website, and get the pH value!""")
