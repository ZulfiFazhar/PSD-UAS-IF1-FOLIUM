import streamlit as st
from utils import init

st.set_page_config(page_title="Dashboard IF-1 FOLIUM", page_icon="🗺️", layout="wide")


init()

st.title("Dashboard")

st.write('''
    Data yang dibahas di dashboard ini adalah E-Commerce Public Dataset. Data ini memiliki informasi lebih dari 100 ribu jumlah transaksi yang terjadi di Brazil.         
''')