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
us = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1aje6O6XELpsv7vYE0uaRMyHd3q-a9yNt").content))
choose = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1fFSYxhHA37S6_pBv3dytJe3OzR1Pqkwj").content))

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
us1, us2 = st.columns([3, 1])
with us1:
    st.write("""
             ### What is pHocus Smart Patch?
             pHocus Smartpatch combines cutting-edge **wound care** and **pH monitoring** to **enhance healing, track progress, and predict recovery outcomes** through **innovative technology**.
             """)
with us2:
    st.image(us)

# Why pHocus
st.write("""
### Why pHocus Smart Patch?
""")
st.image(choose, width=500)