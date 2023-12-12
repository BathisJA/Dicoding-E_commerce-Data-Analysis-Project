import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
products = pd.read_csv('data/products_updated.csv')
order_items = pd.read_csv('data/order_items_dataset.csv')
sellers = pd.read_csv('data/sellers_dataset.csv')

# Pertanyaan No. 1
merged_order_products = pd.merge(order_items, products, on='product_id', how='left')
product_sales = merged_order_products.groupby(['product_id', 'product_category_name']).size().reset_index(name='total_sales')
top_selling_product = product_sales.loc[product_sales['total_sales'].idxmax()]

# Pertanyaan No. 2
seller_counts = sellers['seller_city'].value_counts()
top_cities = seller_counts.head(5)


# Streamlit App
st.title('Dashboard Analisis Data E-commerce')

# Sidebar with project info
st.sidebar.subheader('Informasi Proyek')
st.sidebar.write('Dibuat oleh Bathistuta Jiwandono Aji')
st.sidebar.write('Proyek ini bertujuan untuk menganalisis data e-commerce dan menyajikannya dalam bentuk dashboard interaktif.')
st.sidebar.write('Data diperoleh dari https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce')


# Pertanyaan No. 1
st.subheader('Pertanyaan No. 1: Produk dengan Penjualan Terbanyak')

# Visualisasi Top 10 Produk dengan Penjualan Terbanyak
fig_product_sales = plt.figure(figsize=(12, 6))
bar_plot_products = sns.barplot(x='product_category_name', y='total_sales',
                                data=product_sales.sort_values(by='total_sales', ascending=False).head(10),
                                palette='viridis', hue='product_category_name', dodge=False, legend=False)
for p in bar_plot_products.patches:
    bar_plot_products.annotate(format(p.get_height(), '.0f'),
                                (p.get_x() + p.get_width() / 2., p.get_height()),
                                ha='center', va='center',
                                xytext=(0, 9),
                                textcoords='offset points')
st.pyplot(fig_product_sales)

# Conclusion for Pertanyaan No. 1
st.write("""
Berdasarkan chart bar diatas dapat disimpulkan bahwa produk furniture dan dekorasi menempati posisi pertama dengan jumlah penjualan terbanyak, yaitu 527. 
Sedangkan perlengkapan rumah tangga menempati posisi kesepuluh dengan jumlah penjualan paling sedikit, yaitu 239. 
Hal ini menunjukkan bahwa produk furniture dan dekorasi memiliki permintaan yang tinggi dari konsumen.
""")

# Pertanyaan No. 2
st.subheader('Pertanyaan No. 2: Top 5 Kota dengan Jumlah Seller Terbanyak')

# Visualisasi
fig_top_cities = plt.figure(figsize=(12, 6))
bar_plot_cities = sns.barplot(x=top_cities.values, y=top_cities.index, hue=top_cities.index, palette='viridis', dodge=False)

if bar_plot_cities.legend_ is not None:
    bar_plot_cities.legend_.remove()

for p in bar_plot_cities.patches:
    plt.annotate(format(p.get_width(), '.0f'),
                 (p.get_width(), p.get_y() + p.get_height() / 2.),
                 ha='left', va='center',
                 xytext=(10, 0),
                 textcoords='offset points')

# Conclusion for Pertanyaan No. 2
st.write("""
Berdasarkan chart bar di bawah, dapat disimpulkan bahwa 5 kota dengan jumlah seller terbanyak di Brasil adalah:
- Sao Paulo (694)
- Curitiba (127)
- Rio de Janeiro (96)
- Belo Horizonte (68)
- Ribeirao Preto (52)

Kota Sao Paulo memiliki jumlah seller terbanyak, yaitu 694 seller. Sedangkan kota Ribeirao Preto memiliki jumlah seller paling sedikit, yaitu 52 seller. 
Maka dapat dibuat kesimpulan bahwa terdapat perbedaan yang cukup signifikan antara jumlah seller di kota Sao Paulo dengan kota-kota lainnya. 
Hal ini menunjukkan bahwa kota Sao Paulo merupakan pusat bisnis dan perdagangan di Brasil, sehingga banyak seller yang berpusat di kota tersebut.
""")

# Display the plot in Streamlit
st.pyplot(fig_top_cities)

st.caption('Copyright © Bathistuta Jiwandono Aji 2023')