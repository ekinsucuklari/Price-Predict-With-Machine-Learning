import streamlit as st
import pandas as pd
from joblib import load

# Random Forest modelini yükleme
model = load("C:/Users/LENOVO/Desktop/Ekinsu Eylül ASLAN 222802003/algoritmalar/rf_model.joblib")

st.title("Fiyat Tahmini Uygulaması")

# Seçim kutucukları ile kullanıcıdan veri alma
Fren_Tipi = st.selectbox("Fren Tipi Seçiniz", ["V Fren", "Hidrolik Disk Fren", "Mekanik Disk Fren", "Hidrolik Fren", "Disk Fren"])
Jant = st.selectbox("Jant Seçiniz", ["18.0", "20.0", "24.0", "26.0", "27.50", "28.0", "29.0"])
Materyal = st.selectbox("Materyal Seçiniz", ["Çelik", "Alüminyum", "Karbon"])
Renk = st.selectbox("Renk Seçiniz", ["Siyah", "Gri", "Mavi", "Sarı", "Kırmızı", "Beyaz", "Yeşil", "Pembe", "Turuncu", "Turkuaz", "Lacivert", "Bej", "Mor", "Haki", "Çok Renkli", "Altın", "Kahverengi", "Bordo"])
Vites = st.selectbox("Vites Seçiniz", ["7", "8", "10", "11", "12", "16", "18", "21", "22", "24", "26", "27", "30"])


# Giriş vektörü
input_data = [Fren_Tipi, Jant, Materyal, Renk, Vites]  

# Dönüşüm fonksiyonunu tanımlama
def transform_input_to_numeric(input_data):
    mapping_dict = {
        "V Fren": 4,
        "Hidrolik Disk Fren": 1,
        "Mekanik Disk Fren": 3,
        "Hidrolik Fren": 2,
        "Disk Fren":0,
        "18.0": 0,
        "20.0": 1,
        "24.0": 2,
        "26.0": 3,
        "27.50": 4,
        "28.0": 5,
        "29.0": 6,
        "Çelik": 2,
        "Alüminyum": 0,
        "Karbon": 1,
        "Siyah": 13,
        "Gri": 4,
        "Mavi": 9,
        "Sarı": 12,
        "Kırmızı": 7,
        "Beyaz": 2,
        "Yeşil": 16,
        "Pembe": 11,
        "Turuncu": 15,
        "Turkuaz": 14,
        "Lacivert": 8,
        "Bej": 1,
        "Mor": 10,
        "Haki": 5,
        "Çok Renkli": 17,
        "Altın": 0,
        "Kahverengi": 6,
        "Bordo": 3,
        "7": 11,
        "8": 12,
        "10": 0,
        "11": 1,
        "12": 2,
        "16": 3,
        "18": 4,
        "21": 5,
        "22": 6,
        "24": 7,
        "26": 8,
        "27": 9,
        "30": 10,
        
    }
    numeric_input_data = [mapping_dict[val] for val in input_data]

    return numeric_input_data

# Button to trigger prediction
if st.button("Tahmin Yap"):
    # Dönüşüm fonksiyonunu kullanarak giriş verisini numerik formata çevirin
    numeric_input_data = transform_input_to_numeric(input_data)

    # Modelden tahmin alın
    prediction = model.predict([numeric_input_data])

    # Tahmin sonuçlarını gösterin
    st.subheader(f"Tahmini Fiyat: {prediction[0]:.3f}")
