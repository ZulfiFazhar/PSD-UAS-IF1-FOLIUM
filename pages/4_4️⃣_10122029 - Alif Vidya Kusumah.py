import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import init

st.set_page_config(page_title="Alif", page_icon="4️⃣", layout="wide")

init()

st.title("Alif Vidya Kusumah - 10122029")

st.write(
    """
    #### Informasi yang akan disampaikan pada dashboard ini adalah tentang perbandingan berat produk antara pengiriman yang mengalami keterlambatan dengan yang tidak mengalami keterlambatan
    """
)
with st.expander("Kegunaan dari informasi ini"):
    st.write('''Perbandingan berat produk antara pengiriman yang terlambat dan tidak terlambat krusial untuk menilai kualitas layanan penjual dan kurir dalam hal pengiriman. Informasi ini juga membantu memahami urgensi perbaikan sistem pengiriman, terutama dalam konteks ketepatan waktu yang sangat penting bagi pelanggan. Analisis berat produk menjadi landasan evaluasi yang memungkinkan pengurangan keterlambatan pengiriman dan peningkatan kepuasan pelanggan.''')

# Load data
prod_ords_df = pd.read_csv('dataset/alif-prod_ords_df.csv')

# Menampilkan dataframe
st.dataframe(prod_ords_df)

# Menambahkan garis pemisah
st.write('<hr>', unsafe_allow_html=True)

st.header('Grafik Perbandingan Rata-Rata Berat Produk Dalam Pengiriman')

# Menghitung rata-rata berat produk untuk pengiriman terlambat
weight_late_delivered_mean = prod_ords_df[prod_ords_df['late_delivered']
                                          == True]['product_weight_g'].mean()

# Menghitung rata-rata berat produk untuk pengiriman tepat waktu atau tidak terlambat
weight_notlate_delivered_mean = prod_ords_df[prod_ords_df['late_delivered']
                                             == False]['product_weight_g'].mean()

# Menampilkan informasi rata-rata berat produk dalam tabel
avg_weight_data = {
    'Status Pengiriman': ['Pengiriman Terlambat', 'Pengiriman Tidak Terlambat'],
    'Rata-Rata Berat Produk (gram)': [weight_late_delivered_mean, weight_notlate_delivered_mean]
}

avg_weight_df = pd.DataFrame(avg_weight_data)
st.table(avg_weight_df)

# Menampilkan grafik perbandingan rata-rata berat produk
plt.figure(figsize=(6, 5))
bar_heights = [weight_late_delivered_mean, weight_notlate_delivered_mean]
bar_labels = ['Pengiriman Terlambat', 'Pengiriman Tidak Terlambat']
plt.bar(bar_labels, bar_heights, color=['#FF6347', '#32CD32'])
plt.title('Perbandingan Rata-Rata Berat Produk')
plt.xlabel('Status Pengiriman')
plt.ylabel('Rata-Rata Berat Produk (gram)')
plt.ylim(0, max(bar_heights) + 200)

# Menambahkan label pada bar
for i, height in enumerate(bar_heights):
    plt.text(i, height + 50, f'{height:.2f}', ha='center')

# Menampilkan grafik menggunakan streamlit
st.pyplot(plt)

# Menambahkan penjelasan dari grafik
with st.expander("Penjelasan dari grafik ini"):
    st.write(
        "Berdasarkan analisis data, ditemukan bahwa jumlah pengiriman yang mengalami keterlambatan memiliki rata-rata berat produk sebesar 2471.68, sementara pengiriman yang tidak terlambat memiliki rata-rata berat produk sebesar 2069.27. Temuan ini menunjukkan adanya korelasi atau pengaruh antara berat produk dan keterlambatan pengiriman. Rata-rata berat produk yang lebih tinggi pada pengiriman yang terlambat mengindikasikan bahwa berat produk dapat menjadi faktor yang mempengaruhi tingkat keterlambatan dalam proses pengiriman. Interpretasi ini dapat menjadi dasar untuk langkah-langkah perbaikan dalam manajemen logistik guna mengoptimalkan efisiensi pengiriman dan mengurangi kemungkinan keterlambatan di masa mendatang.")
