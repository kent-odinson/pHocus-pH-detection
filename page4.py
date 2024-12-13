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
url5 = "https://drive.google.com/uc?export=download&id=1Vaiutx8UktOjT_k1QpLD7V7RjWqN3yAT"
response5 = requests.get(url5)
url6 = "https://drive.google.com/uc?export=download&id=1ijbwFP43NehEwuosPz11dmX46B5rboXn"
response6 = requests.get(url6)
url7 = "https://drive.google.com/uc?export=download&id=1ySTOr2vCN15akwJpB_jVJCooNEZcAvv2"
response7 = requests.get(url7)
url8 = "https://drive.google.com/uc?export=download&id=1TwnmclaTGC348v6iqA8_OcUYINPI1DpA"
response8 = requests.get(url8)
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
tit1, tit2 = st.columns([1,3])
with tit1:
    st.image(logo, width=300)
with tit2:
    st.write("## pHocus Smart Patch")
st.write("""
##### A pH detector to measure your skin pH from just a photo of patch!
""")

# About section
st.write("#### Meet The Team: Kelompok 1 Desain Proyek Teknik Biomedik 2021")
team1, team2 = st.columns([1,3])
with team1:
    st.image(syafa)
    st.image(debby)
    st.image(kent)
    st.image(zahra)
with team2:
    st.write("""
             #### Syafamillah Tsabitah
             2106631816

             #### Debby Rofiko Malik
             2106705000

             #### Kent Frederick Wirawan
             2106706760

             #### Fatimah Azzahra
             2106732235""")