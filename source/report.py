import pandas as pd
import plotly.express as px
import streamlit as st
from plotly import graph_objects as go

st.title('Reporte de Informe mediante Gráficos')

st.subheader('1.  Cantidad de Número de Repitencias por Año de Ingreso:')
#-------------------------------------------------------------------------------------------


datos = pd.read_csv('./data/REPITENCIAS_POR_ANIO_INGRESO.csv')
st.write(datos) 