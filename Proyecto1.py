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



df8 = pd.read_excel('8_Monitoreo_Enero_2021.xlsx')

df=pd.concat([df8], axis=0, ignore_index=True)
df
