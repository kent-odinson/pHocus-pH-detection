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

response1 = requests.get("https://drive.google.com/uc?export=download&id=1Tj0anph6-lVTRn16FVwWivIYU027Tosy")
response5 = requests.get("https://drive.google.com/uc?export=download&id=1Vaiutx8UktOjT_k1QpLD7V7RjWqN3yAT")
response6 = requests.get("https://drive.google.com/uc?export=download&id=1ijbwFP43NehEwuosPz11dmX46B5rboXn")
response7 = requests.get("https://drive.google.com/uc?export=download&id=1ySTOr2vCN15akwJpB_jVJCooNEZcAvv2")
response8 = requests.get("https://drive.google.com/uc?export=download&id=1TwnmclaTGC348v6iqA8_OcUYINPI1DpA")
logo = Image.open(BytesIO(response1.content))
syafa = Image.open(BytesIO(response5.content))
debby = Image.open(BytesIO(response6.content))
kent = Image.open(BytesIO(response7.content))
zahra = Image.open(BytesIO(response8.content))

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
tit1, tit2 = st.columns([1,4])
with tit1:
    st.image(logo, width=300)
with tit2:
    st.write("## pHocus Smart Patch")
st.write("""
##### A pH detector to measure your skin pH from just a photo of patch!
""")

# About section
st.write("#### Meet The Team: Kelompok 1 Desain Proyek Teknik Biomedik 2021")
team1, team2 = st.columns([1,5])
with team1:
    st.image(syafa, width=100)
    st.image(debby, width=100)
    st.image(kent, width=100)
    st.image(zahra, width=100)
with team2:
    st.write("""
             #### Syafamillah Tsabitah
             2106631816""")
    st.write("")
    st.write("""
             #### Debby Rofiko Malik
             2106705000""")
    st.write("")
    st.write("""
             #### Kent Frederick Wirawan
             2106706760""")
    st.write("")
    st.write("""
             #### Fatimah Azzahra
             2106732235""")