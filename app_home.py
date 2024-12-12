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

# Multiple Page
st.set_page_config(page_title="pHocus Smart Patch", layout="centered", initial_sidebar_state="auto", page_icon= initial)
main_page = st.Page("page1.py", title="Main Page", icon=":material/home:")
second_page = st.Page("page2.py", title="What To Do", icon=":material/help:")
third_page = st.Page("page3.py", title="Run", icon=":material/directions_run:")
fourth_page = st.Page("page4.py", title="The Team", icon=":material/groups:")
pg = st.navigation([main_page, second_page, third_page, fourth_page])
pg.run()