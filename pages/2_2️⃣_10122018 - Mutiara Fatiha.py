import streamlit as st
from utils import init
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Mutiara", page_icon="3️⃣", layout="wide")

init()

st.title("Mutiara Fatiha - 10122018")

st.write(
    '''
    #### Informasi yang akan disampaikan pada dasboard ini adalah tentang grafik peringkat penjualan barang sesuai katagori.
'''
)

with st.expander("Kegunaan informasi ini"):
    st.write(
        '''
        Informasi yang diberikan oleh grafik peringkat penjualan sesuai kategori memiliki beberapa kegunaan yang penting, terutama dalam konteks analisis bisnis dan pengambilan keputusan. 
'''
    )

st.write('<hr>', unsafe_allow_html=True)



st.header('Grafik Peringkat Penjualan Berdasarkan Kategori')

cat_rank_df = pd.read_csv('dataset/mutiara-cat_rank.csv')
st.dataframe(cat_rank_df)

cat_rank_top = cat_rank_df.head(10)
fig, ax = plt.subplots(figsize=(16,6))
bars = ax.bar(cat_rank_top['product_category_name_english'], cat_rank_top['count'], width=0.5, align='center', color=['#5d9c59','#C6F1D6','#C6F1D6','#C6F1D6','#C6F1D6','#C6F1D6','#C6F1D6','#C6F1D6','#C6F1D6','#C6F1D6'])

ax.set_xlabel('Kategori')
ax.set_ylabel('Jumlah Penjualan')

for bar, count in zip(bars, cat_rank_top['count']):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, str(count), ha='center', va='bottom')

plt.show()
st.pyplot(plt)

with st.expander('Penjelasan grafik peringkat penjualan'):
    st.write(
        '''
        Grafik peringkat penjualan sesuai kategori adalah visualisasi data yang menunjukkan sejauh mana setiap kategori berperforma dalam hal penjualan. Grafik ini biasanya menampilkan kategori-kategori 
        produk atau layanan yang diurutkan berdasarkan besaran penjualan mereka. 
'''
    )

