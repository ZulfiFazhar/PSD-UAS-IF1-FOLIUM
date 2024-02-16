import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import init

st.set_page_config(page_title="Alif", page_icon="4️⃣", layout="wide")

init()

st.title("Alif Vidya Kusumah")

st.write(
    """
        #### Informasi yang akan disampaikan pada dashboard ini adalah tentang perbandingan berat produk antara pengiriman yang mengalami keterlambatan dan dengan yang tidak mengalami tidak keterlambatan
"""
)
with st.expander("Kegunaan dari informasi ini"):
    st.write('''Informasi perbandingan berat produk antara pengiriman yang mengalami keterlambatan dan yang tidak mengalami keterlambatan memiliki kegunaan yang potensial dalam mengevaluasi efisiensi dan kualitas layanan logistik. Dengan membandingkan berat produk pada kedua kondisi pengiriman tersebut, perusahaan dapat mengidentifikasi potensi masalah atau kesalahan yang mungkin terjadi selama proses pengiriman yang mengalami keterlambatan. Informasi ini dapat digunakan sebagai indikator kinerja logistik, membantu perusahaan untuk meningkatkan manajemen rantai pasok dan mengoptimalkan proses pengiriman guna mengurangi kemungkinan terjadinya keterlambatan di masa mendatang. Selain itu, perbandingan berat produk juga dapat memberikan wawasan tentang keandalan dan ketepatan waktu pihak pengiriman, yang dapat menjadi dasar untuk pengambilan keputusan yang lebih baik dalam pemilihan mitra logistik. ''')


prod_ords_df = pd.read_csv('dataset/alif-prod_ords_df.csv')

st.dataframe(prod_ords_df)

st.write('<hr>', unsafe_allow_html=True)

weight_late_delivered_mean = prod_ords_df[prod_ords_df['late_delivered']
                                          == True]['product_weight_g'].mean()
st.write(
    f'Rata-rata berat produk yang mengalami keterlambatan pengiriman : {weight_late_delivered_mean:.2f}')
weight_notlate_delivered_mean = prod_ords_df[prod_ords_df['late_delivered']
                                             == False]['product_weight_g'].mean()
st.write(
    f'Rata-rata berat produk yang tidak mengalami keterlambatan pengiriman : {weight_notlate_delivered_mean:.2f}')

plt.figure(figsize=(6, 5))
bar_heights = [weight_late_delivered_mean, weight_notlate_delivered_mean]
bar_labels = ['Pengiriman Terlambat', 'Pengiriman Tidak Terlambat']
plt.bar(bar_labels, bar_heights, color=['#FF6347', '#32CD32'])
plt.title('Perbandingan Rata-Rata Berat Produk')
plt.xlabel('Status Pengiriman')
plt.ylabel('Rata-Rata Berat Produk (gram)')
plt.ylim(0, max(bar_heights) + 200)
for i, height in enumerate(bar_heights):
    plt.text(i, height + 50, f'{height:.2f}', ha='center')
plt.show()
st.pyplot(plt)
with st.expander("Penjelasan dari grafik ini"):
    st.write('''Berdasarkan analisis rata-rata yang telah dilakukan, terlihat bahwa terdapat perbedaan rata-rata berat produk antara pengiriman yang mengalami keterlambatan dengan yang tidak. Rata-rata berat produk pada pengiriman yang terlambat cenderung lebih tinggi dengan total 2471.68 dibandingkan dengan pengiriman yang tepat waktu atau tidak terlambat dengan total 2069.27, dapat diasumsikan bahwa adanya hubungan antara berat produk dengan keterlambatan pengiriman.''')
