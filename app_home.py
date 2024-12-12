# ==================================================
# MAIN PAGE FOR PHOCUS SMART PATCH
# ==================================================
# Import Libraries
import streamlit as st
import numpy as np

# Input Needed Image
from PIL import Image
import requests
from io import BytesIO

url2 = "https://drive.google.com/uc?export=download&id=1U1mWRiB-Tj5kC9krER5h_tup7veb4LdJ"
response2 = requests.get(url2)
initial = Image.open(BytesIO(response2.content))

# Multiple Page
st.set_page_config(page_title="pHocus Smart Patch", layout="centered", initial_sidebar_state="auto", page_icon= initial)
main_page = st.Page("page1.py", title="Main Page", icon=":material/home:")
second_page = st.Page("page2.py", title="What To Do", icon=":material/help:")
third_page = st.Page("page3.py", title="Run", icon=":material/directions_run:")
fourth_page = st.Page("page4.py", title="The Team", icon=":material/groups:")
pg = st.navigation([main_page, second_page, third_page, fourth_page])
pg.run()