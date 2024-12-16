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
wound = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1oU6px7JjOl7hAktKa2JZjU5z4-9TRy0c").content))
apply = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1aHtRfhKT0Idh49yMkQuDFo7jMKA9ULhZ").content))
reaction = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1zuWM1aKm2S5B1tbQM87WQHeOPmbJ615a").content))

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
step1, step2 = st.columns([1,4])
with step1:
    st.image(wound, width=400)
    st.image(apply, width=400)
    st.image(reaction, width=400)
with step2:
    st.write("""
             #### Ouch!
             Your skin is damaged! Quick treat it as soon as possible!
             #### Apply!
             Place the pHocus Smartpatch securely on the wound
             #### React!
             Allow the patch to change color based on the wound's pH level""")