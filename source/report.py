import pandas as pd
import plotly.express as px
import streamlit as st
from plotly import graph_objects as go

st.title('Reporte de Informe mediante Gráficos')

# ------------------------------------------------------------------------------------------
st.subheader('1. Repitencias más Críticas:')

df_0 = pd.read_csv('./data/REPITENCIAS_CRITICAS.csv')
st.write(df_0)

fig_0 = px.line(df_0, x = 'Número de Repitencias', y='Cantidad de Repitencias Críticas', width=900,
                    height=460,markers=True,
                    color_discrete_sequence = px.colors.qualitative.Light24)

fig_0.update_traces(line_color='#0000ff')
fig_0.update_layout(xaxis_title= 'Número de Repitencias', yaxis_title='Cantidad de Repitencias')
st.plotly_chart(fig_0) 

#-------------------------------------------------------------------------------------------
st.subheader('1. Cantidad de Número de Repitencias por Año de Ingreso:')

@st.cache(allow_output_mutation=True)
def load_data(nrows):
    datos = pd.read_csv('./data/REPITENCIAS_POR_ANIO_INGRESO.csv', nrows=nrows)
    datos.fillna(0, inplace=True)
    return datos

df_1 = pd.read_csv('./data/REPITENCIAS_POR_ANIO_INGRESO.csv')
df_1.fillna(0, inplace=True)

df_load_state = st.text('Cargando data ...')
datos = load_data(20)

if st.checkbox('Mostrar datos crudos'):
    st.subheader('Datos')
    st.write(datos)

fig_1 = px.line(df_1, x = 'Año', y=df_1.columns[1:7], width=900, height=460,markers=True,
                    color_discrete_sequence = px.colors.qualitative.Light24)
fig_1.update_layout(xaxis_title= 'Año de Ingreso', yaxis_title='Cantidad de Repitencias',
                        legend_title='Número de Repitencias')
st.plotly_chart(fig_1) 

# -----------------------------------------------------------------------------------------
st.subheader('2. Cantidad de Número de Repitencias por Facultad:')
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
fig_4.update_layout(width=1000, height=500)

fig_4.add_trace(go.Funnel(name='1era Repitencia', orientation='h',y = df_4['Nombre de Área'],x = df_4['1era Repitencia'],
                marker = {'color': ['deepskyblue','deepskyblue','deepskyblue','deepskyblue','deepskyblue']}))

fig_4.add_trace(go.Funnel(name='2da Repitencia', orientation='h',y = df_4['Nombre de Área'],x = df_4['2da Repitencia'],
                marker = {'color': ['indianred','indianred','indianred','indianred','indianred']}))

fig_4.add_trace(go.Funnel(name='3ra Repitencia', orientation='h',y = df_4['Nombre de Área'],x = df_4['3ra Repitencia'],
                marker = {'color': ['teal','teal','teal','teal','teal']}))
st.plotly_chart(fig_4)

#----------------------------------------------------------------------------------------------------------
st.subheader('5. Porcentaje de Créditos Aprobados por Área:')

df_5 = pd.read_csv('./data/PORCENTAJE_DE_CREDITOS_APROBADOS_POR_AREA.csv')
df_5.fillna(0, inplace=True)

fig_5 = px.line(df_5, x= 'Área', y=df_5.columns[1:13], width=1100, height=550, markers=True,
                    color_discrete_sequence = px.colors.qualitative.Light24_r)
fig_5.update_layout(xaxis_title= 'Área Académica', yaxis_title='Cantidad de Porcentaje de Créditos Aprobados',
                        legend_title='Intervalos de Porcentaje')

st.plotly_chart(fig_5)
# --------------------------------------------------------------------------------------------------------

st.subheader('6. Top 10 de Facultades con mayores Repitencias en total 2023-0:')
df_6 = pd.read_csv('./data/TOTAL_DE_REPITENCIAS_POR_FACULTAD.csv')
df_6 = df_6.reset_index(drop=True)
df_6 = df_6.head(10)

fig_6 = px.line_polar(df_6, r='Total de Repitencias', theta='Facultad',line_close=True,
                    color_discrete_sequence = px.colors.sequential.RdBu_r)
fig_6.update_traces(fill ='toself')
fig_6.update_layout(legend_title='Número de Repitencias')
fig_6.update_layout(width=900, height=550)
fig_6.update_layout(margin=dict(t=110))

st.plotly_chart(fig_6)

# --------------------------------------------------------------------------------------------------------
st.subheader('7. Top 20 de Cursos con mayor número de Repitencias 2023-0:')
df_7 = pd.read_csv('./data/REPITENCIAS_POR_CURSO.csv')
df_7 = df_7.sort_values('Total Repitencias',ascending=False)
df_7 = df_7.reset_index(drop=True)
df_7 = df_7.head(20)

fig_7 = px.bar(df_7, y='Total Repitencias', x='Cursos',text_auto = True,
       orientation = 'v',color = 'Total Repitencias', color_continuous_scale = 'viridis')
fig_7.update_layout(width=1000, height=650)
fig_7.update_layout(xaxis_title= 'Cursos', yaxis_title='Cantidad de Repitencias',
                        legend_title='Cantidad de Repitencias')
fig_7.update_xaxes(tickangle=28, tickfont=dict(color='white', size=11))
st.plotly_chart(fig_7)