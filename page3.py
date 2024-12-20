# ==================================================
# PAGE 3 : PH DETECTION
# ==================================================
# Import Libraries
import streamlit as st
import numpy as np
import pickle

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

# User Input
import cv2
st.write("### Input Photo")
predict = st.file_uploader("", type=["jpg", "jpeg", "png"])
res = 0

# Extract Color Value
def data(m):
    mm = np.asarray(m, dtype=np.uint8)
    image = cv2.imdecode(mm, 1)
    BGR_avg = list(map(float, cv2.mean(image)[:3]))
    print(BGR_avg)

    Gray = (BGR_avg[0]*0.114 + BGR_avg[1]*0.587 + BGR_avg[2]*0.299) or 1.0
    Xb = BGR_avg[0]/Gray
    Xg = BGR_avg[1]/Gray
    Xr = BGR_avg[2]/Gray
    l1 = [Gray,Xb,Xg,Xr]

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    HSV_avg = list(map(float, cv2.mean(hsv)[:3]))

    lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    Lab_avg = list(map(float, cv2.mean(lab)[:3]))

    c = BGR_avg + l1 + HSV_avg + Lab_avg

    return c

# Load Regression Function Using Pickle
ph = pickle.load(BytesIO(requests.get("https://raw.githubusercontent.com/kent-odinson/pHocus-pH-detection/main/mlmodel.pkl").content))

if predict is not None:
    # Display the uploaded image
    hai = bytearray(predict.read())
    image = Image.open(predict)
    st.image(image, use_container_width=True)
    
    # Data Processing
    res = round(ph.predict([data(hai)])[0],2)

# Prediction Output
d = res - 5.5
dcolor=""
if d==0:
    dcolor = "off"
elif d<=0:
    dcolor = "normal"
elif d>=0:
    dcolor = "inverse"
st.metric("### Prediction Results", value=res, delta=d, delta_color=dcolor)

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
