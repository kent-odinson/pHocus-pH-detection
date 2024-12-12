# ==================================================
# PAGE 4 : THE TEAM
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
tit1, tit2 = st.columns([4, 3])
with tit1:
    st.header("pHocus Smart Patch")
    st.write("### Heal. Track. Predict.")
with tit2:
    st.image(logo)
st.write("""
##### A pH detector to measure your skin pH from just a photo of patch!
""")

# About section
st.write(""" #### Meet The Team: Kelompok 1 Desain Proyek Teknik Biomedik 2021
Debby Rofiko Malik (2106705000)
Syafamillah Tsabitah (2106631816)  
Kent Frederick Wirawan(2106706760)
Fatimah Azzahra (2106732235)
""")