import streamlit as st
import pandas as pd
from utils import init

st.set_page_config(page_title="Zulfi", page_icon="2️⃣", layout="wide")

init()

st.title("Zulfi Fadilah Azhar")

state_count = pd.read_csv('dataset/zulfi-state_count.csv')

st.dataframe(state_count)