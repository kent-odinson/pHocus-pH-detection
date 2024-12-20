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

logo = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1EuzviqgyPz8Ve-jUqounzMGFLfBKKAQz").content))
syafa = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1Vaiutx8UktOjT_k1QpLD7V7RjWqN3yAT").content))
debby = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1ijbwFP43NehEwuosPz11dmX46B5rboXn").content))
kent = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1ySTOr2vCN15akwJpB_jVJCooNEZcAvv2").content))
zahra = Image.open(BytesIO(requests.get("https://drive.google.com/uc?export=download&id=1TwnmclaTGC348v6iqA8_OcUYINPI1DpA").content))

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
st.write("### Meet The Team: Kelompok 1 Desain Proyek Teknik Biomedik 2021")
team1, team2 = st.columns([1,5])
with team1:
    st.image(syafa, width=100)
    st.image(debby, width=100)
    st.image(kent, width=100)
    st.image(zahra, width=100)
with team2:
    st.write("""
             #### Syafamillah Tsabitah
             PIC for Patch Finalization and Analysis""")
    st.write("")
    st.write("""
             #### Debby Rofiko Malik
             PIC for 3D Modelling and Environment Box""")
    st.write("")
    st.write("""
             #### Kent Frederick Wirawan
             PIC for Machine Learning and User Interface""")
    st.write("")
    st.write("""
             #### Fatimah Azzahra
             PIC for Patch Making and Prototype Testing""")
