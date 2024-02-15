import streamlit as st
from utils import init
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Izza", page_icon="5️⃣", layout="wide")

init()

st.title("Dawla Izza Al-Din Noor - 10122034")

st.write(
    """
        #### Informasi yang akan disampaikan pada dashboard ini adalah tentang persentase pengiriman barang yang terjadi keterlambatan dan hubungan keterlambatan pengiriman dengan review yang diberikan oleh customer    
"""
)
with st.expander("Kegunaan dari informasi ini"):
    st.write('''Informasi ini akan sangat berguna untuk melihat kualitas pelayanan dari penjual dan kurir dalam bagian pengiriman, sehingga dapat menjadi bahan evaluasi. Dari informasi ini juga dapat diketahui seberapa pentingnya ketepatan waktu sebuah pengiriman bagi customer, sehingga dapat diketahui tingkat urgensi dari perbaikan sistem pengiriman sebagai upaya untuk mengurangi angka keterlambatan pengiriman.''')

# Load data
order_review_late_df = pd.read_csv('dataset/izza-order_review_late.csv')


st.write('<hr>', unsafe_allow_html=True)

st.header("Grafik Persentase Keterlambatan Pengiriman")

# Menghitung jumlah pengiriman terlambat
delivery_late_sum = len(order_review_late_df[order_review_late_df['delivered_late']])
# Menghitung jumlah pengiriman tepat waktu
delivery_notLate_sum = len(order_review_late_df) - delivery_late_sum
# Persentase pengiriman yang terlambat
delivery_late_percentage = (delivery_late_sum / len(order_review_late_df)) * 100
# Persentase pengiriman yang tepat waktu
delivery_notLate_percentage = 100 - delivery_late_percentage

st.dataframe({
    'Kategori': ['Pengiriman Terlambat', 'Pengiriman Tepat Waktu'],
    'Jumlah': [delivery_late_sum, delivery_notLate_sum],
    'Persentase': [f'{delivery_late_percentage:.2f} %', f'{delivery_notLate_percentage:.2f} %']
})

pie_sizes = [delivery_late_percentage, delivery_notLate_percentage]
pie_labels = ['Pengiriman Terlambat', 'Pengiriman Tidak Terlambat']
fig, ax = plt.subplots()
ax.pie(pie_sizes, labels=pie_labels, explode=(0.05, 0), autopct='%1.2f%%', startangle=140, colors=['#DF2E38','#5D9C59'])
ax.axis('equal') 
st.pyplot(fig)

with st.expander("Penjelasan persentase keterlambatan pengiriman"):
    st.write(
        '''
        Dari hasil analisis data tersebut, didapatkan bahwa jumlah keterlambatan pengiriman adalah sebanyak 6409 dari 89952 pengiriman yang berhasil terkirim atau sebanyak 6.65% dari total pengiriman. Hasil tersebut menunjukan angka keterlambatan yang cukup tinggi sehingga perlu adanya evaluasi kualitas jasa di bagian pengiriman. 
        '''
    )


st.write('<hr>', unsafe_allow_html=True)

st.header('Grafik Perbandingan Rata-Rata Skor Review')

# Rata-rata skor review pada pengiriman yang terlambat
late_score_mean = order_review_late_df[order_review_late_df['delivered_late']]['review_score'].mean()
# Rata-rata skor review pada pengiriman yang tidak terlambat
not_late_score_mean = order_review_late_df[order_review_late_df['delivered_late'] == False]['review_score'].mean()

bar_heights = [late_score_mean, not_late_score_mean]
bar_labels = ['Pengiriman Terlambat', 'Pengiriman Tidak Terlambat']

fig, ax = plt.subplots()
ax.bar(bar_labels, bar_heights, color=['#DF2E38','#5D9C59'])
ax.set_ylabel('Rata-rata Skor Review')

for i in range (len(bar_labels)) :
    ax.text(bar_labels[i], bar_heights[i], f'{bar_heights[i]:.2f}', ha='center', va='bottom' )

st.pyplot(fig)

with st.expander("Penjelasan perbandingan rata-rata skor review"):
    st.write(
        '''
        Dari grafik terlihat bahwa rata-rata skor review yang diberikan oleh pembeli pada pengiriman yang terlambat jauh lebih rendah dibandingkan pada pengiriman yang tidak terlambat. Pada pengiriman yang terlambat rata-rata skor review adalah 2.27, sedangkan pada pengiriman yang tidak terlambat rata-rata skor review adalah 4.29. Hal ini menunjukan bahwa ketepatan waktu pengiriman sangat penting bagi pembeli, sehingga pencarian solusi untuk mengurangi angka keterlambatan pengiriman menjadi sangat relevan dan penting.

'''
    )


st.write('<hr>', unsafe_allow_html=True)
st.header('Grafik Penyebaran Skor Review pada Pengiriman yang Terlambat')

# Menghitung penyebaran skor review
review_counts = order_review_late_df[order_review_late_df['delivered_late']]['review_score'].value_counts()
review_counts_df = pd.DataFrame(review_counts)
review_counts_df.reset_index(inplace=True)
# Menghitung total review
total_review = review_counts_df['count'].sum()
# Menghitung persentase skor review
review_counts_df['percentage'] = (review_counts_df['count'] / total_review) * 100

st.dataframe(review_counts_df)

fig, ax = plt.subplots()
ax.bar(review_counts_df['review_score'], review_counts_df['count'], color=['#9E1711','#D65D42','#D65D42','#D65D42','#D65D42'], width=0.8)
ax.set_ylabel('Frekuensi (Pelanggan)')

for i in review_counts_df.index :
    row_data = review_counts_df.loc[i]
    ax.text(row_data['review_score'], row_data['count'], f'{row_data["count"]} ({row_data["percentage"]:.2f} %)', ha='center', va='bottom', fontsize=8)

st.pyplot(fig)

with st.expander("Penjelasan penyebaran skor review pada pengiriman yang terlambat"):
    st.write(
        '''
        Dari grafik tersebut, terlihat bahwa pelanggan yang mengalami keterlambatan pengiriman sangat cenderung untuk memberikan skor review yang sangat rendah. Sebesar 53% pelanggan yang mengalami keterlambatan pengiriman memberikan skor review 1 (sangat buruk). Hal ini menunjukan bahwa ketepatan waktu pengiriman sangat penting bagi pelanggan. 
'''
    )