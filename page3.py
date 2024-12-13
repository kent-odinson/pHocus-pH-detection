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
tit1, tit2 = st.columns([3, 4])
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

# Extract Color Value
import cv2
import os
import csv


def data(m):
    BGR_avg = list(map(float, cv2.mean(img)[:3]))

    Gray = BGR_avg[0]*0.114 + BGR_avg[1]*0.587 + BGR_avg[2]*0.299
    Xb = BGR_avg[0]/Gray
    Xg = BGR_avg[1]/Gray
    Xr = BGR_avg[2]/Gray
    l1 = [Gray,Xb,Xg,Xr]

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    HSV_avg = list(map(float, cv2.mean(hsv)[:3]))

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
    Lab_avg = list(map(float, cv2.mean(lab)[:3]))

    c = BGR_avg + l1 + HSV_avg + Lab_avg

    return c

with open("C:/Users/ASUS/Documents/(())/Semester 7/Despro 2/pH Detection Using Smartphone/answer.csv", "a", newline='') as f: #filepath save CSV file
    writer = csv.writer(f)
    writer.writerow(["B","G","R","Gray","Xb","Xg","Xr","H","S","V","L","a","b"])
    img = cv2.imread(predict)
    writer.writerow(data(img) + f)

# Load Regression Function Using Pickle
import pickle
ph = pickle.load(open('mlmodel.pkl', 'rb'))

# Data Processing
res = ph.predict(predict)

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