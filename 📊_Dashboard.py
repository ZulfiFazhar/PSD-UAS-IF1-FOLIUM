import streamlit as st
from utils import init

@st.cache_data
st.set_page_config(page_title="Dashboard IF-1 FOLIUM", page_icon="🗺️", layout="wide")


init()

st.title("Dashboard")