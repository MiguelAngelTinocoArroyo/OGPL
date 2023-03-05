import pandas as pd
import plotly.express as px
import streamlit as st
from plotly import graph_objects as go

st.title('Reporte de Informe mediante Gráficos')

# ------------------------------------------------------------------------------------------
st.subheader('1. Repitencias más Críticas por estudiante:')

@st.cache(allow_output_mutation=True)
def load_data_1(nrows):
    datos_1 = pd.read_csv('./data/REPITENCIAS_CRITICAS.csv', nrows=nrows)
    return datos_1

df_load_state = st.text('Cargando data ...')
datos_1 = load_data_1(6)

if st.checkbox('Mostrar datos'):
    st.subheader('Datos')
    st.write(datos_1)

df_1 = pd.read_csv('./data/REPITENCIAS_CRITICAS.csv')

fig_1 = px.line(df_1, x = 'Número de Repitencias', y='Cantidad de Repitencias Críticas', width=700,
                    height=460,markers=True,
                    color_discrete_sequence = px.colors.qualitative.Light24)

fig_1.update_traces(line_color='#0000ff')
fig_1.update_layout(xaxis_title= 'Número de Repitencias', yaxis_title='Cantidad de Repitencias')
st.plotly_chart(fig_1) 

#-------------------------------------------------------------------------------------------
st.subheader('2. Cantidad de Número de Repitencias por Año de Ingreso:')

@st.cache(allow_output_mutation=True)
def load_data_2(nrows):
    datos_2 = pd.read_csv('./data/REPITENCIAS_POR_ANIO_INGRESO.csv', nrows=nrows)
    datos_2.fillna(0, inplace=True)
    return datos_2

df_2 = pd.read_csv('./data/REPITENCIAS_POR_ANIO_INGRESO.csv')
df_2.fillna(0, inplace=True)

df_load_state = st.text('Cargando data ...')
datos_2 = load_data_2(20)

if st.checkbox('Mostrar datos 2'):
    st.subheader('Datos')
    st.write(datos_2)

fig_2 = px.line(df_2, x = 'Año', y=df_2.columns[1:7], width=900, height=460,markers=True,
                    color_discrete_sequence = px.colors.qualitative.Light24)
fig_2.update_layout(xaxis_title= 'Año de Ingreso', yaxis_title='Cantidad de Repitencias',
                        legend_title='Número de Repitencias')
st.plotly_chart(fig_2) 

# -----------------------------------------------------------------------------------------
st.subheader('3. Cantidad de Número de Repitencias por Facultad:')
df_3 = pd.read_csv('./data/REPITENCIAS_POR_FACULTAD.csv')
fig_3 = px.line(df_3, x= 'Facultad', y=df_3.columns[1:7], width=1000, height=600, markers=True,
                    color_discrete_sequence = px.colors.qualitative.Light24_r)
fig_2.update_layout(xaxis_title= 'Facultad', yaxis_title='Cantidad de Repitencias',
                        legend_title='Número de Repitencias')

st.plotly_chart(fig_3)

# -----------------------------------------------------------------------------------------
st.subheader('4. Top 10 de Facultades por Escuela Académicas Profesionales con mayores Repitencias:')

df_4 = pd.read_csv('./data/REPITENCIAS_POR_FACULTAD_Y_EAP.csv')
df_4.fillna(0, inplace=True)

df_4 = df_4.sort_values('Repitencias',ascending=False)
df_4 = df_4.reset_index(drop=True)
df_4 = df_4.head(10)

fig_4 = px.sunburst(df_4, path=['Facultad','Escuela Académica'], values= 'Repitencias', 
                color_continuous_scale=px.colors.sequential.Cividis_r, 
                width=1000, height=600, color='Repitencias')

fig_4.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')

st.plotly_chart(fig_4)

# ------------------------------------------------------------------------------------------------------------------
st.subheader('5. Repitencias por Área:')
df_5 = pd.read_csv('./data/REPITENCIAS_POR_AREA.csv')
df_5 = df_5.sort_values('1era Repitencia', ascending=False)

from plotly import graph_objects as go

fig_5 = go.Figure()
fig_5.update_layout(width=1000, height=500)

fig_5.add_trace(go.Funnel(name='1era Repitencia', orientation='h',y = df_5['Nombre de Área'],x = df_5['1era Repitencia'],
                marker = {'color': ['deepskyblue','deepskyblue','deepskyblue','deepskyblue','deepskyblue']}))

fig_5.add_trace(go.Funnel(name='2da Repitencia', orientation='h',y = df_5['Nombre de Área'],x = df_5['2da Repitencia'],
                marker = {'color': ['indianred','indianred','indianred','indianred','indianred']}))

fig_5.add_trace(go.Funnel(name='3ra Repitencia', orientation='h',y = df_5['Nombre de Área'],x = df_5['3ra Repitencia'],
                marker = {'color': ['teal','teal','teal','teal','teal']}))
st.plotly_chart(fig_5)

#----------------------------------------------------------------------------------------------------------
st.subheader('6. Porcentaje de Créditos Aprobados por Área:')

df_6 = pd.read_csv('./data/PORCENTAJE_DE_CREDITOS_APROBADOS_POR_AREA.csv')
df_6.fillna(0, inplace=True)

fig_6 = px.line(df_6, x= 'Área', y=df_6.columns[1:13], width=1100, height=550, markers=True,
                    color_discrete_sequence = px.colors.qualitative.Light24_r)
fig_6.update_layout(xaxis_title= 'Área Académica', yaxis_title='Cantidad de Porcentaje de Créditos Aprobados',
                        legend_title='Intervalos de Porcentaje')

st.plotly_chart(fig_6)
# --------------------------------------------------------------------------------------------------------

st.subheader('7. Top 10 de Facultades con mayores Repitencias en total 2023-0:')
df_7 = pd.read_csv('./data/TOTAL_DE_REPITENCIAS_POR_FACULTAD.csv')
df_7 = df_7.reset_index(drop=True)
df_7 = df_7.head(10)

fig_7 = px.line_polar(df_7, r='Total de Repitencias', theta='Facultad',line_close=True,
                    color_discrete_sequence = px.colors.sequential.RdBu_r)
fig_7.update_traces(fill ='toself')
fig_7.update_layout(legend_title='Número de Repitencias')
fig_7.update_layout(width=900, height=550)
fig_7.update_layout(margin=dict(t=110))

st.plotly_chart(fig_7)

# --------------------------------------------------------------------------------------------------------
st.subheader('8. Top 20 de Cursos con mayor número de Repitencias 2023-0:')
df_8 = pd.read_csv('./data/REPITENCIAS_POR_CURSO.csv')
df_8 = df_8.sort_values('Total Repitencias',ascending=False)
df_8 = df_8.reset_index(drop=True)
df_8 = df_8.head(20)

fig_8 = px.bar(df_8, y='Total Repitencias', x='Cursos',text_auto = True,
       orientation = 'v',color = 'Total Repitencias', color_continuous_scale = 'viridis')
fig_8.update_layout(width=1000, height=650)
fig_8.update_layout(xaxis_title= 'Cursos', yaxis_title='Cantidad de Repitencias',
                        legend_title='Cantidad de Repitencias')
fig_8.update_xaxes(tickangle=28, tickfont=dict(color='white', size=11))
st.plotly_chart(fig_8)