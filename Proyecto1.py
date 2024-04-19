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


df1 = pd.read_excel('Monitoreo_julio.xlsx')
df2 = pd.read_excel('Monitoreo_agosto.xlsx')
df3 = pd.read_excel('Monitoreo_setiembre_Bonilla.xlsx')
df4 = pd.read_excel('Monitoreo_setiembre_Ov.Miraflores.xlsx')
df5 = pd.read_excel('Monitoreo_octubre.xlsx')
df6 = pd.read_excel('6_Monitoreo_Noviembre.xlsx')
df7 = pd.read_excel('7_Monitoreo_Diciembre.xlsx')
df8 = pd.read_excel('8_Monitoreo_Enero_2021.xlsx')
df9 = pd.read_excel('9_Monitoreo_Febrero_2021.xlsx')
df10 = pd.read_excel('10_Monitoreo_Marzo_2021.xlsx')
df11 = pd.read_excel('11_Monitoreo_Abril_2021.xlsx')
df12 = pd.read_excel('12_Monitoreo_Mayo_2021.xlsx')
df13 = pd.read_excel('13_Monitoreo_Junio_2021.xlsx')
df=pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13], axis=0, ignore_index=True)
df
