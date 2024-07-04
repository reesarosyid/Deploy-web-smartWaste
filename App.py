import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import base64
from streamlit_option_menu import option_menu
import pickle
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from statsmodels.tsa.arima.model import ARIMAResults

# Menambahkan dua logo di bagian atas
def add_single_logo(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    st.markdown(f"""
    <style>
    .logo {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
    }}
    .logo img {{
        width: 350px;  # Anda bisa mengubah ukuran sesuai kebutuhan
        margin: 10px;  # Memberi jarak jika diperlukan
    }}
    </style>
    <div class="logo">
        <img src="data:image/png;base64,{bin_str}" alt="Logo">
    </div>
    """, unsafe_allow_html=True)

# Ganti dengan path gambar logo Anda
add_single_logo("dlh.png")

# Dataframe pertama (dataset asli)
data1 = [
    {"tahun": "2019", "Daun Terolah(KG)": 0.0, "Kompos Jadi(KG)": 4130.0, "Sampah Daun(KG)": 0.0, "Sampah Fermentasi(KG)": 0.0, "Sampah Sayur(KG)": 0.0},
    {"tahun": "2020", "Daun Terolah(KG)": 7073.0, "Kompos Jadi(KG)": 3175.0, "Sampah Daun(KG)": 9867.0, "Sampah Fermentasi(KG)": 16669.0, "Sampah Sayur(KG)": 6200.0},
    {"tahun": "2021", "Daun Terolah(KG)": 6331.0, "Kompos Jadi(KG)": 2630.0, "Sampah Daun(KG)": 12465.0, "Sampah Fermentasi(KG)": 13529.0, "Sampah Sayur(KG)": 6377.0},
    {"tahun": "2022", "Daun Terolah(KG)": 6844.0, "Kompos Jadi(KG)": 2805.0, "Sampah Daun(KG)": 12542.0, "Sampah Fermentasi(KG)": 15608.0, "Sampah Sayur(KG)": 6851.0},
    {"tahun": "2023", "Daun Terolah(KG)": 7221.0, "Kompos Jadi(KG)": 4090.0, "Sampah Daun(KG)": 16100.0, "Sampah Fermentasi(KG)": 16574.0, "Sampah Sayur(KG)": 8868.0},
    {"tahun": "2024", "Daun Terolah(KG)": 1111.0, "Kompos Jadi(KG)": 525.0, "Sampah Daun(KG)": 2440.0, "Sampah Fermentasi(KG)": 2142.0, "Sampah Sayur(KG)": 1145.0},
]

# Membuat dataframe pertama
df1 = pd.DataFrame(data1)

# Dataframe kedua (dataset baru)
data2 = [
    {"tahun": "2019", "Daun Terolah(KG)": 0.0, "Kompos Jadi(KG)": 4130.0, "Sampah Daun(KG)": 0.0, "Sampah Fermentasi(KG)": 0.0, "Sampah Sayur(KG)": 0.0},
    {"tahun": "2020", "Daun Terolah(KG)": 7493.0, "Kompos Jadi(KG)": 3805.0, "Sampah Daun(KG)": 10328.0, "Sampah Fermentasi(KG)": 12540.0, "Sampah Sayur(KG)": 13334.0},
    {"tahun": "2021", "Daun Terolah(KG)": 7315.0, "Kompos Jadi(KG)": 3120.0, "Sampah Daun(KG)": 12018.0, "Sampah Fermentasi(KG)": 12385.0, "Sampah Sayur(KG)": 8655.0},
    {"tahun": "2022", "Daun Terolah(KG)": 8458.0, "Kompos Jadi(KG)": 3575.0, "Sampah Daun(KG)": 12579.0, "Sampah Fermentasi(KG)": 12965.0, "Sampah Sayur(KG)": 9231.0},
    {"tahun": "2023", "Daun Terolah(KG)": 6664.0, "Kompos Jadi(KG)": 5535.0, "Sampah Daun(KG)": 13000.0, "Sampah Fermentasi(KG)": 17149.0, "Sampah Sayur(KG)": 15577.0},
    {"tahun": "2024", "Daun Terolah(KG)": 1257.0, "Kompos Jadi(KG)": 915.0, "Sampah Daun(KG)": 3010.0, "Sampah Fermentasi(KG)": 2963.0, "Sampah Sayur(KG)": 2505.0},
]

# Membuat dataframe kedua
df2 = pd.DataFrame(data2)

# Dataframe ketiga
data3 = [
    {"Tahun": "2020", "SUM(Daun Terolah)": 14589.0, "SUM(Sampah Daun)": 20205.0, "SUM(Sampah Fermentasi)": 25608.0, "SUM(Sampah Sayuran)": 12098.0},
    {"Tahun": "2021", "SUM(Daun Terolah)": 13236.0, "SUM(Sampah Daun)": 24123.0, "SUM(Sampah Fermentasi)": 26969.0, "SUM(Sampah Sayuran)": 15412.0},
    {"Tahun": "2022", "SUM(Daun Terolah)": 15302.0, "SUM(Sampah Daun)": 25211.0, "SUM(Sampah Fermentasi)": 28563.0, "SUM(Sampah Sayuran)": 16264.0},
    {"Tahun": "2023", "SUM(Daun Terolah)": 5745.0, "SUM(Sampah Daun)": 12022.0, "SUM(Sampah Fermentasi)": 16230.0, "SUM(Sampah Sayuran)": 15297.0},
    {"Tahun": "2024", "SUM(Daun Terolah)": 2368.0, "SUM(Sampah Daun)": 5450.0, "SUM(Sampah Fermentasi)": 5105.0, "SUM(Sampah Sayuran)": 3650.0}
]

# Membuat dataframe ketiga
df3 = pd.DataFrame(data3)

# Dataframe keempat
data4 = [
    {"Bulan": "January", "2020": 150.0, "2021": 760.0, "2022": 760.0, "2023": 635.0, "2024": 350.0},
    {"Bulan": "February", "2020": 175.0, "2021": 600.0, "2022": 600.0, "2023": 0.0, "2024": 1090.0},
    {"Bulan": "March", "2020": 150.0, "2021": 700.0, "2022": 700.0, "2023": 1215.0, "2024": None},
    {"Bulan": "April", "2020": 1010.0, "2021": 725.0, "2022": 725.0, "2023": 280.0, "2024": None},
    {"Bulan": "May", "2020": 950.0, "2021": 700.0, "2022": 700.0, "2023": 420.0, "2024": None},
    {"Bulan": "June", "2020": 675.0, "2021": 0.0, "2022": 0.0, "2023": 0.0, "2024": None},
    {"Bulan": "July", "2020": 510.0, "2021": 445.0, "2022": 445.0, "2023": 356.0, "2024": None},
    {"Bulan": "August", "2020": 625.0, "2021": 325.0, "2022": 325.0, "2023": 625.0, "2024": None},
    {"Bulan": "September", "2020": 540.0, "2021": 455.0, "2022": 455.0, "2023": 975.0, "2024": None},
    {"Bulan": "October", "2020": 500.0, "2021": 300.0, "2022": 300.0, "2023": 0.0, "2024": None},
    {"Bulan": "November", "2020": 735.0, "2021": 740.0, "2022": 735.0, "2023": 835.0, "2024": None},
    {"Bulan": "December", "2020": 635.0, "2021": 300.0, "2022": 635.0, "2023": 0.0, "2024": None}
]

# Membuat dataframe keempat
df4 = pd.DataFrame(data4)

# Dataframe kelima (data baru)
data5 = [
    {"Kompos": "Jatirejo", "SUM(Kompos Jadi)": 13365},
    {"Kompos": "Pasar Kendal", "SUM(Kompos Jadi)": 8125}
]

# Membuat dataframe kelima
df5 = pd.DataFrame(data5)

#Data set ke 6 data harian
df6 = pd.read_csv("Laporan hasil Rumah Kompos gabungan harian.csv")
df6.head()

# membuat dataframe keenam
df = pd.DataFrame (df6)

# NAVIGASI
selected = option_menu(
    menu_title=None,  # Hide the menu title
    options=["Home", "Dataframe", "Tambah Data", "About"],  # Options in the navbar
    icons=["house", "table", "plus-circle"],  # Icons for each option
    menu_icon="cast",  # Menu icon
    default_index=0,  # Default active option
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#00000"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {
            "font-size": "20px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "green"},
    },
)

# Define the content for each section
if selected == "Home":
    st.title("Smart Waste Manajement")
    def create_box(content, font_size='100px'):
        st.markdown(f"""
    <style>
    .box {{
        padding: 20px;
        margin: 10px 0;
        border: 2px solid #000;
        border-radius: 10px;
        background-color: #123523;
    }}
    </style>
    <div class="box">
        {content}
    </div>
    """, unsafe_allow_html=True)

# Creating a box with custom content
    create_box("Proyek Smart Waste Manajemen merupakan Sub Project dari Center of Excellence Universitas Dian Nuswantoro yang bekerja sama dengan Dinas Lingkungan Hidup Kabupaten Kendal. Bertujuan untuk mengembangkan solusi inovatif dalam pengelolaan sampah yang lebih efisien dan ramah lingkungan. Dengan meningkatnya jumlah penduduk dan urbanisasi, volume sampah yang dihasilkan terus bertambah, sehingga diperlukan sistem pengelolaan sampah yang cerdas dan terintegrasi. Proyek ini menggabungkan teknologi IoT (Internet of Things), big data, dan kecerdasan buatan (Artificial Intelligence) untuk mengoptimalkan proses pengumpulan, pengangkutan, dan pembuangan sampah.")
elif selected == "Dataframe":
    st.title("Tabel Data")
    st.write("Tabel Data Analis Total Hasil Kompos Kabupaten Kendal  :")
    st.write(df5)
    st.write("Tabel Data Analis Rumah Kompos Tahunan:")
    st.write(df3)
    col1, col2 = st.columns(2)

    # Menampilkan plot pertama menggunakan Streamlit
    with col1:
        st.write("Tabel Data Analis Rumah Kompos Pasar  Kendal:")
        st.write(df1)

    # Menampilkan plot kedua menggunakan Streamlit
    with col2:
        st.write("Tabel Data Analis Rumah Kompos Jatirejo:")
        st.write(df2)
    st.write("Tabel Data Hasil kompos pada rumah kompos Gabungan:")
    st.write(df4)
    st.write("Tabel data harian Rumah Kompos gabungan: ")
    st.write(df6)

#elif selected == "Polychart": (Menggudupkan polychart )
    st.title("Chart Visualisasi")

     #Plotly chart using plotly.graph_objects
    labels = df5['Kompos']
    values = df5['SUM(Kompos Jadi)']
    fig5 = go.Figure(data=[go.Pie(labels=labels, values=values)])
    # Update layout untuk plot kelima
    fig5.update_layout(
        
    title='Kompos Distribution'
    )

    st.plotly_chart(fig5)

    # Menampilkan char data 1 dan data 2
    fig1 = go.Figure()
    for column in df1.columns[1:]:  # Exclude 'tahun' column
        fig1.add_trace(go.Bar(x=df1['tahun'], y=df1[column], name=column))

    fig1.update_layout(
        barmode='group',
        title='Data 1: Akumulasi Rumah Kompos Tahunan Pasar Kendal',
        xaxis_title='Tahun',
        yaxis_title='Jumlah (KG)',
        legend_title='Kategori'
    )

    # Plotly chart using plotly.graph_objects for data 2
    fig2 = go.Figure()
    for column in df2.columns[1:]:  # Exclude 'tahun' column
        fig2.add_trace(go.Bar(x=df2['tahun'], y=df2[column], name=column))
 
        fig2.update_layout(
            barmode='group',
            title='Data 2: Akumulasi Rumah Kompos Tahunan Jatirejo',
            xaxis_title='Tahun',
            yaxis_title='Jumlah (KG)',
            legend_title='Kategori'
        )

    # Membuat dua kolom
    col1, col2 = st.columns(2)

   # Menampilkan plot pertama menggunakan Streamlit
    with col1:
        st.plotly_chart(fig1)

    # Menampilkan plot kedua menggunakan Streamlit
    with col2:
        st.plotly_chart(fig2)

    # Menampilkan Chart data 3
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=df3['Tahun'], y=df3['SUM(Daun Terolah)'], mode='lines+markers', name='SUM(Daun Terolah)'))
    fig3.add_trace(go.Scatter(x=df3['Tahun'], y=df3['SUM(Sampah Daun)'], mode='lines+markers', name='SUM(Sampah Daun)'))
    fig3.add_trace(go.Scatter(x=df3['Tahun'], y=df3['SUM(Sampah Fermentasi)'], mode='lines+markers', name='SUM(Sampah Fermentasi)'))
    fig3.add_trace(go.Scatter(x=df3['Tahun'], y=df3['SUM(Sampah Sayuran)'], mode='lines+markers', name='SUM(Sampah Sayuran)'))

    # Update layout untuk plot ketiga
    fig3.update_layout(
        title='Analisis Manajemen Sampah Tahunan ',
        xaxis_title='Tahun',
        yaxis_title='Jumlah (KG)',
        legend_title='Kategori'
    )
    st.plotly_chart(fig3)

    # Menampilkan Chart data ke 4
    # Membuat plot untuk dataset keempat
    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(x=df4['Bulan'], y=df4['2020'], mode='markers', name='2020'))
    fig4.add_trace(go.Scatter(x=df4['Bulan'], y=df4['2021'], mode='markers', name='2021'))
    fig4.add_trace(go.Scatter(x=df4['Bulan'], y=df4['2022'], mode='markers', name='2022'))
    fig4.add_trace(go.Scatter(x=df4['Bulan'], y=df4['2023'], mode='markers', name='2023'))
    fig4.add_trace(go.Scatter(x=df4['Bulan'], y=df4['2024'].fillna(0), mode='markers', name='2024'))

    # Update layout untuk plot keempat
    fig4.update_layout(
        title='Hasil kompos pada rumah kompos Gabungan',
        xaxis_title='Bulan',
        yaxis_title='Jumlah (KG)',
        legend_title='Tahun',
        xaxis=dict(type='category')
    )
    st.plotly_chart(fig4)

    st.title("Model Mechine Learning")

    # Load the ARIMA model
    
    
    def forecast(df, model, feature):
        df['Date'] = pd.to_datetime(df[['Tahun', 'Bulan']].assign(DAY=1).astype(str).agg('-'.join, axis=1))
        df.set_index('Date', inplace=True)
        ts_data = df[feature].dropna()

    # Load the model from the file
        with open(model, 'rb') as file:
            loaded_model = pickle.load(file)

    # Assuming ts_data and df are defined previously
    # ts_data: the original time series data
    # df: a DataFrame that includes the in-sample forecast

        # Calculate in-sample forecast
        df['forecast_in_sample'] = loaded_model.predict_in_sample()

        # Calculate out-of-sample forecast
        forecast_out_sample = loaded_model.predict(n_periods=12)  # Forecast for the next 12 months

        # Create the index for the out-sample forecast
        out_sample_index = pd.date_range(start=ts_data.index[-1], periods=13, freq='M')[1:]

        # Combine in-sample and out-sample forecasts
        combined_forecast = pd.concat([df['forecast_in_sample'], pd.Series(forecast_out_sample, index=out_sample_index)])

        # Plotting with Plotly
        fig6 = make_subplots()

        # Original time series data
        fig6.add_trace(go.Scatter(
            x=ts_data.index,
            y=ts_data,
            mode='lines+markers',
            name='Original',
            line=dict(color='blue'),
            marker=dict(symbol='circle')
        ))

        # In-sample forecast
        fig6.add_trace(go.Scatter(
            x=df.index,
            y=df['forecast_in_sample'],
            mode='lines+markers',
            name='Forecast (In-sample)',
            line=dict(color='green'),
            marker=dict(symbol='circle')
        ))

        # Out-of-sample forecast
        fig6.add_trace(go.Scatter(
            x=out_sample_index,
            y=forecast_out_sample,
            mode='lines+markers',
            name='Forecast (Out-sample)',
            line=dict(color='green'),
            marker=dict(symbol='circle')
        ))

        # Adding a connection between the last in-sample point and the first out-sample point
        fig6.add_trace(go.Scatter(
            x=[df.index[-1], out_sample_index[0]],
            y=[df['forecast_in_sample'].iloc[-1], forecast_out_sample[0]],
            mode='lines+markers',
            line=dict(color='green'),
            marker=dict(symbol='circle'),
            showlegend=False
        ))

        # Update layout
        fig6.update_layout(
            title=f'Time Series {feature} Forecast',
            xaxis_title='Date',
            yaxis_title='Value',
            legend=dict(x=0, y=1),
            xaxis=dict(showgrid=True),
            yaxis=dict(showgrid=True)
        )

        # Tampilkan plot menggunakan st.plotly_chart
        st.plotly_chart(fig6)

        #pemanggilan tampilan
        #col3, col4 = st.columns(2)
        #with col3:
            #df_bulanan adalah nama dataset
        #    forecast(file_path, "Model/model_sampahDaun.pkl", "Sampah Daun")
    
#Tambah Data Tabel Data Analis Total Hasil Kompos Kabupaten Kendal
elif selected == "Tambah Data":
    # Path to your CSV file
    file_path = 'Laporan hasil Rumah Kompos Pertahun Pasar Kendal.csv'

        # Read the CSV file
    df = pd.read_csv(file_path)

        # Update the session state with the new DataFrame
    st.session_state.df = df

        # Display the DataFrame
    st.write(st.session_state.df)

    # Initialize the session state with a DataFrame if not already present
    if 'df' not in st.session_state:
        try:
            # Read the CSV file
            df = pd.read_csv(file_path)
        except FileNotFoundError:
            df = pd.DataFrame(columns=[
                "id", "tahun", "bulan", "sampah daun", "sampah sayur",
                "sampah anorganik", "daun terolah", "sampah fermentasi", "kompos jadi"
            ])
        
        st.session_state.df = df

    
    # Function to add data
    def add_data():
        st.subheader('Tambah Data')
        tahun = st.number_input('Tahun', min_value=2000, step=1)
        bulan = st.text_input('Bulan')
        sampah_daun = st.number_input('Sampah Daun', min_value=0, step=1)
        sampah_sayur = st.number_input('Sampah Sayur', min_value=0, step=1)
        sampah_anorganik = st.number_input('Sampah Anorganik', min_value=0, step=1)
        daun_terolah = st.number_input('Daun Terolah', min_value=0, step=1)
        sampah_fermentasi = st.number_input('Sampah Fermentasi', min_value=0, step=1)
        kompos_jadi = st.number_input('Kompos Jadi', min_value=0, step=1)

        if st.button('Tambah'):
            new_row = {
                "tahun": tahun,
                "bulan": bulan,
                "sampah daun": sampah_daun,
                "sampah sayur": sampah_sayur,
                "sampah anorganik": sampah_anorganik,
                "daun terolah": daun_terolah,
                "sampah fermentasi": sampah_fermentasi,
                "kompos jadi": kompos_jadi
            }
            st.session_state.df = pd.concat([st.session_state.df, pd.DataFrame([new_row])], ignore_index=True)
            st.success('Data berhasil ditambahkan')

    # Function to update data
    def update_data():
        st.subheader('Update Data')
        bulan = st.selectbox('Pilih Bulan', st.session_state.df['bulan'].unique())
        if bulan:
            row = st.session_state.df[st.session_state.df['bulan'] == bulan].iloc[0]
            tahun = st.number_input('Tahun', min_value=2000, step=1, value=row['tahun'])
            sampah_daun = st.number_input('Sampah Daun', min_value=0, step=1, value=row['sampah daun'])
            sampah_sayur = st.number_input('Sampah Sayur', min_value=0, step=1, value=row['sampah sayur'])
            sampah_anorganik = st.number_input('Sampah Anorganik', min_value=0, step=1, value=row['sampah anorganik'])
            daun_terolah = st.number_input('Daun Terolah', min_value=0, step=1, value=row['daun terolah'])
            sampah_fermentasi = st.number_input('Sampah Fermentasi', min_value=0, step=1, value=row['sampah fermentasi'])
            kompos_jadi = st.number_input('Kompos Jadi', min_value=0, step=1, value=row['kompos jadi'])

            if st.button('Update'):
                st.session_state.df.loc[st.session_state.df['bulan'] == bulan, ['tahun', 'sampah daun', 'sampah sayur', 'sampah anorganik', 'daun terolah', 'sampah fermentasi', 'kompos jadi']] = [tahun, sampah_daun, sampah_sayur, sampah_anorganik, daun_terolah, sampah_fermentasi, kompos_jadi]
                st.success('Data berhasil diperbarui')

    # Function to delete dat by month
    def delete_data():
        st.subheader('Hapus Data')
        tahun = st.number_input('Tahun untuk Dihapus', min_value=2000, step=1)
        bulan = st.selectbox('Pilih Bulan untuk Dihapus', st.session_state.df['bulan'].unique())
        if st.button('Hapus'):
            st.session_state.df = st.session_state.df[~((st.session_state.df['tahun'] == tahun) & (st.session_state.df['bulan'] == bulan))]
            st.success('Data berhasil dihapus')

    tabs = st.tabs(['Tambah Data', 'Update Data', 'Hapus Data'])

    with tabs[0]:
        add_data()
    with tabs[1]:
        update_data()
    with tabs[2]:
        delete_data()
        
#Berisi tab about bagian belakang 
if selected == "About":
    st.title("Smart Waste Manajement")
    def create_box(content, font_size='100px'):
        st.markdown(f"""
    <style>
    .box {{
        padding: 20px;
        margin: 10px 0;
        border: 2px solid #000;
        border-radius: 10px;
        background-color: #123523;
    }}
    </style>
    <div class="box">
        {content}
    </div
    """, unsafe_allow_html=True)

    #menampilkan dua logo
    def add_single_logo(png_file):
        with open(png_file, "rb") as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        st.markdown(f"""
        <style>
        .logo {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 20px;
        }}
        .logo img {{
            width: 250px;  # Anda bisa mengubah ukuran sesuai kebutuhan
            margin: 10px;  # Memberi jarak jika diperlukan
        }}
        </style>
        <div class="logo">
            <img src="data:image/png;base64,{bin_str}" alt="Logo">
        </div>
        """, unsafe_allow_html=True)
        
    # Main function
def main():
        # Dataset
    df_bulanan = pd.read_excel("Data/Laporan-hasil-Rumah-Kompos-gabungan.xlsx")
            
            # Konversi kolom Tahun ke tipe data datetime
    df_bulanan['Tahun'] = pd.to_datetime(df_bulanan['Tahun'], format='%Y')

            # Tampilkan hanya tahun saja
    df_bulanan['Tahun'] = df_bulanan['Tahun'].dt.year

    #ploty
    col3, col4 = st.columns(2)
    with col3:
        forecast(df_bulanan, "Model/model_sampahDaun.pkl", "Sampah Daun")

    with col4:
        forecast(df_bulanan, "Model/model_sampahSayuran.pkl", "Sampah Sayuran")
        
    col5, col6 = st.columns(2)

    with col5:
        forecast(df_bulanan, "Model/model_daunTerolah.pkl", "Daun Terolah")
    with col6:
        forecast(df_bulanan, "Model/model_sampahFermentasi.pkl", "Sampah Fermentasi")
        
    forecast(df_bulanan, "Model/model_komposJadi.pkl", "Kompos Jadi")

    #untuk yang About
    logos = ["Logo Udinus.png", "logo coe.png"]  # Ganti dengan path/logo Anda
        
    for logo in logos:
            add_single_logo(logo)

if __name__ == "__main__":
    main()