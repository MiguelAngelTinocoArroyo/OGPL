import pandas as pd
import plotly.express as px
import streamlit as st
from plotly import graph_objects as go

st.title('Reporte de Informe mediante Gráficos')

st.subheader('1.  Cantidad de Número de Repitencias por Año de Ingreso:')
#-------------------------------------------------------------------------------------------

df_1 = pd.read_csv('./data/REPITENCIAS_POR_ANIO_INGRESO.csv')
st.write(df_1) 

fig_1 = px.line(df_1, x = 'Año', y=df_1.columns[1:7], width=900, height=460,markers=True,
                    color_discrete_sequence = px.colors.qualitative.Light24)
fig_1.update_layout(xaxis_title= 'Año de Ingreso', yaxis_title='Cantidad de Repitencias',
                        legend_title='Número de Repitencias')
st.plotly_chart(fig_1) 

# -----------------------------------------------------------------------------------------
df_2 = pd.read_csv('./data/REPITENCIAS_POR_FACULTAD.csv')
fig_2 = px.line(df_2, x= 'Facultad', y=df_2.columns[1:7], width=1000, height=600, markers=True,
                    color_discrete_sequence = px.colors.qualitative.Light24_r)
fig_2.update_layout(xaxis_title= 'Facultad', yaxis_title='Cantidad de Repitencias',
                        legend_title='Número de Repitencias')

st.plotly_chart(fig_2)

# -----------------------------------------------------------------------------------------
st.subheader('3. Top 10 de Facultades por Escuela Académicas Profesionales con mayores Repitencias:')

df_3 = pd.read_csv('./data/REPITENCIAS_POR_FACULTAD_Y_EAP.csv')
df_3.fillna(0, inplace=True)

df_3 = df_3.sort_values('Repitencias',ascending=False)
df_3 = df_3.reset_index(drop=True)
df_3 = df_3.head(10)

fig_3 = px.sunburst(df_3, path=['Facultad','Escuela Académica'], values= 'Repitencias', 
                color_continuous_scale=px.colors.sequential.Cividis_r, 
                width=1000, height=600, color='Repitencias')

fig_3.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
fig_3.update_layout(title_text='Top 10 de Facultades por Escuela Académicas Profesionales con mayores Repitencias', title_x=0.5)

st.plotly_chart(fig_3)