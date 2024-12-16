# ==================================================
# PAGE 1 : WHAT IS PHOCUS
# ==================================================
# Import Libraries
import streamlit as st
import numpy as np

# Input Needed Image
from PIL import Image
import requests
from io import BytesIO

logo = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1EuzviqgyPz8Ve-jUqounzMGFLfBKKAQz").content))
expectation = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1diCJUAVNQcu2aRDJZA-afDHRELuhNR_E").content))

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

# What Is pHocus
st.write("""
### What is pHocus Smart Patch?
pHocus Smartpatch combines cutting-edge wound care and pH monitoring to enhance healing, track progress, and predict recovery outcomes through innovative technology.
""")

# Why pHocus
st.write("""
### Why pHocus Smart Patch?

""")

# Expected Outcome
st.write("""
### What Do We Expect?
After the reaction, a new color would be appear of the mixture. But what does the color mean?
""")
st.image(expectation)
exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8 = st.columns(8)
with exp1:
    st.write("  ")
with exp2:
    st.write("Control color")
with exp3:
    st.write("Your skin is dry")
with exp4:
    st.write("Your skin is normal")
with exp5:
    st.write("Your skin is still bleeding")
with exp6:
    st.write("Your skin has a mild bleeding")
with exp7:
    st.write("Your skin has a moderate bleeding")
with exp8:
    st.write("Your skin has a severe bleeding")