# ==================================================
# USER INTERFACE FOR PHOCUS SMART PATCH
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
url2 = "https://drive.google.com/uc?export=download&id=1U1mWRiB-Tj5kC9krER5h_tup7veb4LdJ"
response2 = requests.get(url2)
url3 = "https://drive.google.com/uc?export=download&id=1diCJUAVNQcu2aRDJZA-afDHRELuhNR_E"
response3 = requests.get(url3)
url4 = "https://drive.google.com/uc?export=download&id=18SsN38N21BFjnrfMErqGWRNoaKXtPuQU"
response4 = requests.get(url4)
logo = Image.open(BytesIO(response1.content))
initial = Image.open(BytesIO(response2.content))
expectation = Image.open(BytesIO(response3.content))
step = Image.open(BytesIO(response4.content))

# Page Configuration
st.set_page_config(page_title="pHocus Smart Patch", layout="centered", initial_sidebar_state="auto", page_icon= initial)

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
tit1, tit2 = st.columns([2, 1])
with tit1:
    st.title("pHocus Smart Patch")
with tit2:
    st.image(logo)
st.write("""
##### A machine learning-based pH detector to measure your skin pH from just a photo of patch!
""")

# User Input
st.sidebar.header("Input pHoto")
predict = st.sidebar.file_uploader("", type=["jpg", "jpeg", "png"])

if predict is not None:
    # Display the uploaded image
    image = Image.open(predict)
    st.sidebar.image(image, use_container_width=True)

# enter pH detection model

# Prediction Output
st.write("### Prediction Results")
prediction_result = 6.5
d = prediction_result - 5.5
dcolor=""
if d==0:
    dcolor = "off"
elif d<=0:
    dcolor = "normal"
elif d>=0:
    dcolor = "inverse"
st.metric("pH Detected:", f"{prediction_result:.1f}", delta=d, delta_color=dcolor)

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

# About section
st.write("""
---
### Credits
All credits reserved to Kelompok 1 Desain Proyek Teknik Biomedik 2021:  
Debby Rofiko Malik (2106705000), Syafamillah Tsabitah (2106631816),  
Kent Frederick Wirawan(2106706760), Fatimah Azzahra (2106732235)
""")