import streamlit as st
from utils import init
import pandas as pd

st.set_page_config(page_title="Izza", page_icon="5️⃣", layout="wide")

init()

st.title("Dawla Izza Al-Din Noor")

order_review_late = pd.read_csv('dataset/izza-order_review_late.csv')
st.dataframe(order_review_late)
