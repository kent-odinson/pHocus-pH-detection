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

logo = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1Tj0anph6-lVTRn16FVwWivIYU027Tosy").content))
step = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=18SsN38N21BFjnrfMErqGWRNoaKXtPuQU").content))
apply = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1iBv-87t2uVQAHa4_aCwiBgZDeteUF7SK").content))
wound = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1u_E0hxkcNNPEtVKIlhQ_CRGgsKyjaXlh").content))
reaction = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1QzUK8R_FT8mrU-6kW785VoBeHG80A2DJ").content))

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
step1, step2 = st.columns([3,2])
with step1:
    st.image(wound, width=100)
    st.image(apply, width=100)
    st.image(reaction, width=100)
with step2:
    st.write("""
             #### Ouch!
             You just hurt yourself, and it need treatment as soon as possible!""")
    st.write("")
    st.write("""
             #### Debby Rofiko Malik
             PIC for 3D Modelling and Environment Box""")
    st.write("")
    st.write("""
             #### Kent Frederick Wirawan
             PIC for Machine Learning and User Interface""")
    st.write("")
    st.write("""
             #### Fatimah Azzahra
             PIC for Patch Making and Prototype Testing""")