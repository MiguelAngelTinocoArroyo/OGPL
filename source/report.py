import pandas as pd
import plotly.express as px
import streamlit as st
from plotly import graph_objects as go

st.title('Reporte de Informe mediante Gráficos')

st.subheader('1.  Cantidad de Número de Repitencias por Año de Ingreso:')
#-------------------------------------------------------------------------------------------

df_1 = pd.read_csv('./data/REPITENCIAS_POR_ANIO_INGRESO.csv')
df_1.fillna(0, inplace=True)
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

st.plotly_chart(fig_3)

# ------------------------------------------------------------------------------------------------------------------
st.subheader('4. Repitencias por Área:')
df_4 = pd.read_csv('./data/REPITENCIAS_POR_AREA.csv')
df_4 = df_4.sort_values('1era Repitencia', ascending=False)

from plotly import graph_objects as go

fig_4 = go.Figure()
fig_4.update_layout(width=1100, height=500)

fig_4.add_trace(go.Funnel(name='1era Repitencia', orientation='h',y = df_4['Nombre de Área'],x = df_4['1era Repitencia'],
                marker = {'color': ['deepskyblue','deepskyblue','deepskyblue','deepskyblue','deepskyblue']}))

fig_4.add_trace(go.Funnel(name='2da Repitencia', orientation='h',y = df_4['Nombre de Área'],x = df_4['2da Repitencia'],
                marker = {'color': ['indianred','indianred','indianred','indianred','indianred']}))

fig_4.add_trace(go.Funnel(name='3ra Repitencia', orientation='h',y = df_4['Nombre de Área'],x = df_4['3ra Repitencia'],
                marker = {'color': ['teal','teal','teal','teal','teal']}))
st.plotly_chart(fig_4)

#----------------------------------------------------------------------------------------------------------
st.subheader('5. Porcentaje de Créditos Aprobados por Área:')

df_6 = pd.read_csv('./data/PORCENTAJE_DE_CREDITOS_APROBADOS_POR_AREA.csv')
df_6.fillna(0, inplace=True)

fig_6 = px.line(df_6, x= 'Área', y=df_6.columns[1:13], width=1100, height=550, markers=True,
                    color_discrete_sequence = px.colors.qualitative.Light24_r)
fig_6.update_layout(xaxis_title= 'Área Académica', yaxis_title='Cantidad de Porcentaje de Créditos Aprobados',
                        legend_title='Intervalos de Porcentaje')

st.plotly_chart(fig_6)