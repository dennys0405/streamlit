# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:29:23 2024

@author: den_0
"""

import streamlit as st
import pandas as pd
import numpy as np

st.title('Monitoreo de calidad de aire QAIRA:')
st.write('[Municipalidad de Miraflores]')
num = st.slider("num", 0, 100, step=1)
st.write("El numero ingresado es {}".format(num))

option = st.selectbox(
 '¿Cómo desearía ser contactado/a?',
 ('Email', 'Teléfono', 'Whatsapp'))
st.write('Seleccionó:', option)


n = st.slider("n", 5,100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])
st.line_chart(chart_data)

df = pd.DataFrame(
 np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
 columns=['lat', 'lon'])
st.map(df)
