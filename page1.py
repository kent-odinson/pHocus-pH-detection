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

url1 = "https://drive.google.com/uc?export=download&id=1Tj0anph6-lVTRn16FVwWivIYU027Tosy"
response1 = requests.get(url1)
url3 = "https://drive.google.com/uc?export=download&id=1diCJUAVNQcu2aRDJZA-afDHRELuhNR_E"
response3 = requests.get(url3)
logo = Image.open(BytesIO(response1.content))
expectation = Image.open(BytesIO(response3.content))

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
tit1, tit2 = st.columns(2)
with tit1:
    st.image(logo, width='50%')
with tit2:
    st.header("pHocus Smart Patch")
    st.write("### Heal. Track. Predict.")
st.write("""
##### A pH detector to measure your skin pH from just a photo of patch!
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