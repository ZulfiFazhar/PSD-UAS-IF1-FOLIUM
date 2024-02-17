import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

from utils import init
from wordcloud import WordCloud

st.set_page_config(page_title="Zulfi", page_icon="2️⃣", layout="wide")

init()

# import datasets
state_count = pd.read_csv('dataset/zulfi-state_count.csv')
cust_city_sp = pd.read_csv('dataset/zulfi-cust_city_sp.csv')
top5_cust_city = pd.read_csv('dataset/zulfi-top5_cust_city_sp.csv')

state_count = state_count.head(5)
state_count['Negara Bagian'] = ['São Paulo', 'Minas Gerais', 'Rio de Janeiro', 'Rio Grande do Sul', 'Paraná']
state_count = state_count.reindex(columns=['state', 'Negara Bagian', 'count'])

# membuat function untuk dipanggil nanti
def state_count_visualization(df):
    plt.figure(figsize=(12, 8))
    barplot = sns.barplot(x='Negara Bagian', y='count', data=df, palette='viridis')

    plt.xlabel('Jumlah Pembelian')
    plt.ylabel('State')
    plt.title('Aktifitas pembelian di berbagai state')

    for p in barplot.patches:
        barplot.annotate(format(p.get_height(), '.0f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 10), 
                    textcoords = 'offset points')

    return st.pyplot(plt)

st.title("10122005 - Zulfi Fadilah Azhar")

st.header("Sales Dashboard")

st.write('''
    Dashboard ini berisi informasi penjualan dari negara Brazil. Dari negara tersebut dicari state mana yang memiliki penjualan tertinggi.
''')

def state_view():
    st.subheader('Data Overview')

    col1, col2 = st.columns([1,1.8])

    with col1:
        st.dataframe(state_count.head(5).rename(columns={'state': 'ID', 'count': 'Jumlah Pembelian'}))
        
    with col2:
        st.write('''
    Tabel ini menunjukkan jumlah transaksi yang terjadi di berbagai negara bagian. Berikut adalah penjelasan lebih lanjut:

    - SP: Memiliki jumlah transaksi terbanyak, yaitu 3,878,927 transaksi.
    - MG: Berada di posisi kedua dengan 2,224,871 transaksi.
    - RJ: Berada di posisi ketiga dengan 1,630,246 transaksi.
    - RS: Memiliki 599,746 transaksi.
    - PR: Memiliki 453,088 transaksi.
    ''')
        
    st.write('Dengan data ini, kita dapat melihat bahwa SP adalah negara bagian dengan aktivitas transaksi tertinggi, diikuti oleh MG dan RJ. Sementara itu, RS dan PR memiliki jumlah transaksi yang lebih rendah dibandingkan tiga negara bagian lainnya.')

    st.subheader('Data Visualization')

    state_count_visualization(state_count)

    st.write(''' 
    Dari hasil visualisasi didapati bahwa State of São Paulo merupakan state dengan aktifitas transaksi terbanyak, dengan total sebanyak 3.878.927 (3 juta) transaksi. Langkah yang dapat dilakukan selanjutnya ialah dengan menjadikan state ini sebagai fokus pemasaran lebih mendalam. Karena state ini memiliki 40% aktifitas transaksi dari total 10.328.006 (10 juta) transaksi yang terjadi di Brazil.
    ''')