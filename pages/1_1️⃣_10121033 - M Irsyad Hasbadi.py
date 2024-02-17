import streamlit as st
from utils import init

st.set_page_config(page_title="Irsyad", page_icon="1️⃣", layout="wide")

init()

st.title("M Irsyad Hasbadi")
st.title("Payment Type Informastion")

print("Bisnis Intelligence")
print("1. Mengidentifikasi metode pembayaran yang paling sering digunakan oleh user")
print ("2. Menampilkan jumlah transaksi paling besar untuk setiap metode pembayaran")
print("3. Mendeteksi data transaksi yang tidak sesuai atau bernilai null")

print("1. Business Understanding")
print("2. Memahami Trend dan pola penggunaan metode pembayaran")
print("3. Mengidentifikasi untuk meningkatkan keamanan dan efisiensi pembayaran")

print("Langkah Bisnis")
print("Menyeleksi efisiensi metode pembayaran yang paling sering di gunakan dan tidak atau jarang digunakan")
print("Menawarkan Program loyalitas : Memberikan Accive jika pengguna menggunakan metode pembayaran tertentu")

print("Load Dataset Order_Payment")
data = pd.read_csv("https://raw.githubusercontent.com/ZulfiFazhar/Dicoding-Wrangling-Data/main/dataset/order_payments_dataset.csv")
print(data)

print("Assessing Data Order_Payment")
data.info()

print("Melihat Statistik Deskriptif Dataset")
data.describe()

print("Mencari Missing Value")
data.isnull().sum()

print("Melihat Sampel Data Yang Digunakan")
data.head(10)

print("Identifikasi Value Yang Tidak Memenuhi Standar dengan diagram plot")
data.hist()
plt.show()

print("Proses Cleaning Data")
data.isnull().sum()

print("Melihat Tipe Data Order_Payment")
data.dtypes

print("Menyaring Kolom Kolom Yang Tidak Diperlukan")
data = data.drop(['order_id','payment_sequential'],axis=1)
data

print("Menjumlahkan Value Order_Payment")
payment_type_counts = data['payment_type'].value_counts()
print(payment_type_counts)

print("Menampilkan Payment_Value Yang Terbesar")
max_payment_per_type = data.groupby('payment_type')['payment_value'].max()

print("Nilai pembayaran tertinggi dari masing-masing payment_type:")
print(max_payment_per_type)

st.title("Visualisasi Data")

print("Payment Type Terbanyak Yang Digunakan Dan Payment Type Yang Tidak Terdeteksi")
percentages = round(payment_type_counts / payment_type_counts.sum() * 100, 1)
x = payment_type_counts.values.tolist()

colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
fig, ax = plt.subplots()

wedges, _, _ = ax.pie(x, colors=colors, autopct='',
                      wedgeprops={"linewidth": 1, "edgecolor": "white"}, startangle=90)

labels = [f"{payment_type_counts.index[i]}: {percentages[i]}%" for i in range(len(payment_type_counts))]
plt.legend(wedges, labels, loc="best", bbox_to_anchor=(1, 0.5))

plt.show()

print("Visualisasi Payment_value Tertinggi Dari Masing masing Payment_type")
# max_payment_per_type = data.groupby('payment_type')['payment_value'].max()
display(max_payment_per_type)

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

st.title("Kesimpulan")
print("1. Dari Hasil Perhitungan Terbukti Bahwa Sebanyak 73.9% Customer Memilih Payment Type Berupa Credit Card Dengan Jumlah Transaksi Sebanyak : 76795 Transaksi")
print("2. Terdapat 3 Payment Type Yang Tidak Terdefinisi Di Dalam Dataset")
print("3.Nilai Pyment Value Terbanyak Dari Masing Masing Payment Type Sebagai Berikut :")
print("Boleto : 7274.88")
print("Credit Card : 13664.08")
print("Voucher : 3184.34")
print("Notdefined : 0.00")
print("Payment Value Tertinggi Yang Pernah Dilakukan Yaitu Menggunakan Credit Card Dengan Payment Value Sebanyak :13664.08")




  

