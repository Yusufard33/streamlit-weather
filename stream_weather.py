import pickle 
import numpy as np
import streamlit as st

model = pickle.load(open('weather_model.sav', 'rb'))

st.title('Prediksi Cuaca')

#input
precipitation = st.number_input('Curah')
temp_max = st.number_input('Input Max. Temperature')
temp_min = st.number_input('Input Min. Temperature')
wind = st.number_input('Input Kecepatan Angin')

cuaca = ''

if st.button('Prediksi Cuaca'):
	prediksi = model.predict([[precipitation, temp_max, temp_min, wind]])
	if(prediksi<2):
		cuaca = 'Salju'
	elif(prediksi<3):
		cuaca = 'Hujan'
	elif(prediksi<4):
		cuaca = 'Gerimis'
	elif(prediksi<5):
		cuaca = 'Kabut'
	elif(prediksi<6):
		cuaca = 'Cerah'
	else :
		cuaca = 'Salah'
st.success(cuaca)
