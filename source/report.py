import pandas as pd
import plotly.express as px
import streamlit as st
from plotly import graph_objects as go

st.title('Reporte de Informe mediante Gráficos')

st.subheader('1.  Cantidad de Número de Repitencias por Año de Ingreso:')
#-------------------------------------------------------------------------------------------

def load_data(nrows):
    datos = pd.read_excel('../data/REPITENCIAS_POR_ANIO_INGRESO.xlsx')
    datos.fillna(0, inplace=True)
    return datos

df_load_state = st.text('Cargando data ...')
datos = load_data(1000)

if st.checkbox('Mostrar datos crudos'):
    st.subheader('Datos crudos..')
    st.write(datos)