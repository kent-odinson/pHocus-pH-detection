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

url1 = requests.get("https://drive.google.com/uc?export=download&id=1Tj0anph6-lVTRn16FVwWivIYU027Tosy")
url4 = requests.get("https://drive.google.com/uc?export=download&id=18SsN38N21BFjnrfMErqGWRNoaKXtPuQU")
logo = Image.open(BytesIO(url1.content))
step = Image.open(BytesIO(url4.content))

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
    st.write("## pHocus Smart Patch")
st.write("""
##### A pH detector to measure your skin pH from just a photo of patch!
""")

# How It Works
st.write("""
### How Does It Works?
You've got a patch, and your phone. But what to do with them? Here's some explanation to visualize it:
""")
step1, step2 = st.columns([3,2])
with step1:
    st.image(step)
with step2:
    st.write("1. Put the patch on the wounded area")
    st.write("2. Wait until the reaction done")
    st.write("3. Capture the result, and upload it!")