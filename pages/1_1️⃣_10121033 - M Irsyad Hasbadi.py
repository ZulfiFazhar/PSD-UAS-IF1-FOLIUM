import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils import init

st.set_page_config(page_title="Irsyad", page_icon="1️⃣", layout="wide")

init()

st.title("M Irsyad Hasbadi")
st.title("Payment Type Information")

st.write("Bisnis Intelligence")
st.write("1. Mengidentifikasi metode pembayaran yang paling sering digunakan oleh user")
st.write("2. Menampilkan jumlah transaksi paling besar untuk setiap metode pembayaran")
st.write("3. Mendeteksi data transaksi yang tidak sesuai atau bernilai null")

st.write("Business Understanding")
st.write("2. Memahami Trend dan pola penggunaan metode pembayaran")
st.write("3. Mengidentifikasi untuk meningkatkan keamanan dan efisiensi pembayaran")
>>>>>>> b9cb75d9ba0386b57bcf78227d28854824c89070

st.write("Langkah Bisnis")
st.write("Menyeleksi efisiensi metode pembayaran yang paling sering di gunakan dan tidak atau jarang digunakan")
st.write("Menawarkan Program loyalitas : Memberikan Accive jika pengguna menggunakan metode pembayaran tertentu")

st.write("Load Dataset Order_Payment")
data = pd.read_csv("https://raw.githubusercontent.com/ZulfiFazhar/Dicoding-Wrangling-Data/main/dataset/order_payments_dataset.csv")
st.write(data)

st.write("Assessing Data Order_Payment")
st.write(data.info())

st.write("Melihat Statistik Deskriptif Dataset")
st.write(data.describe())

st.write("Mencari Missing Value")
st.write(data.isnull().sum())

st.write("Melihat Sampel Data Yang Digunakan")
st.write(data.head(10))

st.write("Identifikasi Value Yang Tidak Memenuhi Standar dengan diagram plot")
st.write(data.hist())
plt.show()
st.pyplot(plt)

st.write("Proses Cleaning Data")
st.write(data.isnull().sum())

st.write("Melihat Tipe Data Order_Payment")
st.write(data.dtypes)

st.write("Menyaring Kolom Kolom Yang Tidak Diperlukan")
data = data.drop(['order_id','payment_sequential'],axis=1)
st.write(data)

st.write("Menjumlahkan Value Order_Payment")
payment_type_counts = data['payment_type'].value_counts()
st.write(payment_type_counts)

st.write("Menampilkan Payment_Value Yang Terbesar")
max_payment_per_type = data.groupby('payment_type')['payment_value'].max()
st.write("Nilai pembayaran tertinggi dari masing-masing payment_type:")
st.write(max_payment_per_type)

st.title("Visualisasi Data")

st.write("Payment Type Terbanyak Yang Digunakan Dan Payment Type Yang Tidak Terdeteksi")
percentages = round(payment_type_counts / payment_type_counts.sum() * 100, 1)
x = payment_type_counts.values.tolist()

colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
fig, ax = plt.subplots()

wedges, _, _ = ax.pie(x, colors=colors, autopct='',
                      wedgeprops={"linewidth": 1, "edgecolor": "white"}, startangle=90)

labels = [f"{payment_type_counts.index[i]}: {percentages[i]}%" for i in range(len(payment_type_counts))]
plt.legend(wedges, labels, loc="best", bbox_to_anchor=(1, 0.5))

plt.show()
st.pyplot(plt)

st.write("Visualisasi Payment_value Tertinggi Dari Masing masing Payment_type")
st.write(max_payment_per_type)

plt.figure(figsize=(10, 6))
colors = plt.cm.tab10.colors
max_payment_per_type.plot(kind='bar', color=colors)
plt.xlabel('Metode Pembayaran')
plt.ylabel('Nilai Pembayaran Tertinggi')
plt.title('Nilai Pembayaran Tertinggi per Metode Pembayaran')

for i, value in enumerate(max_payment_per_type):
    plt.text(i, value, f' {value}', ha='center', va='bottom')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
st.pyplot(plt)

st.title("Kesimpulan")
st.write("1. Dari Hasil Perhitungan Terbukti Bahwa Sebanyak 73.9% Customer Memilih Payment Type Berupa Credit Card Dengan Jumlah Transaksi Sebanyak : 76795 Transaksi")
st.write("2. Terdapat 3 Payment Type Yang Tidak Terdefinisi Di Dalam Dataset")
st.write("3.Nilai Pyment Value Terbanyak Dari Masing Masing Payment Type Sebagai Berikut :")
st.write("Boleto : 7274.88")
st.write("Credit Card : 13664.08")
st.write("Voucher : 3184.34")
st.write("Notdefined : 0.00")
st.write("Payment Value Tertinggi Yang Pernah Dilakukan Yaitu Menggunakan Credit Card Dengan Payment Value Sebanyak :13664.08")
