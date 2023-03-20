import pandas as pd
import plotly.express as px
import streamlit as st
from plotly import graph_objects as go

st.set_page_config(layout="wide") # Modo Ancho de Streamlit
st.title('Seguimiento a estudiantes con problemas de repitencias. Prematrícula 2023-0')

# ------------------------------------------------------------------------------------------
st.subheader('1. Repitencias más críticas por estudiante:')

@st.cache(allow_output_mutation=True)
def load_data_1(nrows):
    datos_1 = pd.read_csv('./data/REPITENCIAS_CRITICAS.csv', nrows=nrows)
    return datos_1

df_load_state = st.text('Cargando data ...')
datos_1 = load_data_1(6)

if st.checkbox('Mostrar datos 1'):
    st.subheader('Datos 1')
    st.write(datos_1)

df_1 = pd.read_csv('./data/REPITENCIAS_CRITICAS.csv')

fig_1 = px.line(df_1, x = 'Número de Repitencias', y='Cantidad de Repitencias Críticas', width=800,
                    height=460,markers=True, text = 'Cantidad de Repitencias Críticas',
                    color_discrete_sequence = px.colors.qualitative.Light24)

fig_1.update_traces(line_color='blue')
fig_1.update_layout(xaxis_title= 'Cantidad de Repitencias', yaxis_title='Estudiantes')
fig_1.update_traces(textposition = 'top center')
st.plotly_chart(fig_1) 

#-------------------------------------------------------------------------------------------
st.subheader('2. Número de repitencias totales por año de ingreso:')

@st.cache(allow_output_mutation=True)
def load_data_2(nrows):
    datos_2 = pd.read_csv('./data/REPITENCIAS_POR_ANIO_INGRESO.csv', nrows=nrows)
    datos_2.fillna(0, inplace=True)
    return datos_2

df_2 = pd.read_csv('./data/REPITENCIAS_POR_ANIO_INGRESO.csv')
df_2.fillna(0, inplace=True)

df_load_state = st.text('Cargando data ...')
datos_2 = load_data_2(44)

if st.checkbox('Mostrar datos 2'):
    st.subheader('Datos 2')
    st.write(datos_2)

fig_2 = px.line(df_2, x = 'Año', y=df_2.columns[1:7], width=900, height=460,markers=True,
                    color_discrete_sequence = px.colors.qualitative.Light24)
fig_2.update_layout(xaxis_title= 'Año de Ingreso', yaxis_title='Estudiantes',
                        legend_title='Número de Repitencias')
st.plotly_chart(fig_2) 

# -----------------------------------------------------------------------------------------
st.subheader('3. Número de estudiantes por número de repitencias según facultades:')

@st.cache(allow_output_mutation=True)
def load_data_3(nrows):
    datos_3 = pd.read_csv('./data/REPITENCIAS_POR_FACULTAD.csv', nrows=nrows)
    return datos_3

df_load_state = st.text('Cargando data ...')
datos_3 = load_data_3(20)

if st.checkbox('Mostrar datos 3'):
    st.subheader('Datos 3')
    st.write(datos_3)

df_3 = pd.read_csv('./data/REPITENCIAS_POR_FACULTAD.csv')

fig_3 = px.line(df_3, x= 'Facultad', y=df_3.columns[1:7], width=1000, height=600, markers=True,
                    color_discrete_sequence = px.colors.qualitative.Light24_r)
fig_3.update_layout(xaxis_title= 'Facultad', yaxis_title='Cantidad de Repitencias',
                        legend_title='Número de Repitencias')

st.plotly_chart(fig_3)

# -----------------------------------------------------------------------------------------
st.subheader('4. Top 10 de Programas con mayor número de repitencias:')

@st.cache(allow_output_mutation=True)
def load_data_4(nrows):
    datos_4 = pd.read_csv('./data/REPITENCIAS_POR_FACULTAD_Y_EAP.csv', nrows=nrows)
    datos_4 = datos_4.sort_values('Repitencias',ascending=False)
    datos_4 = datos_4.reset_index(drop=True)
    datos_4 = datos_4.head(10)
    return datos_4

df_load_state = st.text('Cargando data ...')
datos_4 = load_data_4(66)

if st.checkbox('Mostrar datos 4'):
    st.subheader('Datos 4')
    st.write(datos_4)

df_4 = pd.read_csv('./data/REPITENCIAS_POR_FACULTAD_Y_EAP.csv')
df_4.fillna(0, inplace=True)

df_4 = df_4.sort_values('Repitencias',ascending=False)
df_4 = df_4.reset_index(drop=True)
df_4 = df_4.head(10)

fig_4 = px.sunburst(df_4, path=['Facultad','Nombre de Programa'], values= 'Repitencias', 
                color_continuous_scale=px.colors.sequential.Cividis_r, 
                width=950, height=550, color='Repitencias')

fig_4.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')

st.plotly_chart(fig_4)

# ------------------------------------------------------------------------------------------------------------------
st.subheader('5. Número de alumnos por número de repitencias según áreas académicas:')

@st.cache(allow_output_mutation=True)
def load_data_5(nrows):
    datos_5 = pd.read_csv('./data/REPITENCIAS_POR_AREA.csv', nrows=nrows)
    datos_5.fillna(0, inplace=True)
    datos_5 = datos_5.sort_values('Primera repitencia',ascending=False)
    return datos_5

df_load_state = st.text('Cargando data ...')
datos_5 = load_data_5(5)

if st.checkbox('Mostrar datos 5'):
    st.subheader('Datos 5')
    st.write(datos_5)

df_5 = pd.read_csv('./data/REPITENCIAS_POR_AREA.csv')
df_5 = df_5.sort_values('Primera repitencia', ascending=False)

from plotly import graph_objects as go

fig_5 = go.Figure()
fig_5.update_layout(width=1100, height=500)

fig_5.add_trace(go.Funnel(name='Primera repitencia', orientation='h',y = df_5['Área'],x = df_5['Primera repitencia'],
                marker = {'color': ['deepskyblue','deepskyblue','deepskyblue','deepskyblue','deepskyblue']}))

fig_5.add_trace(go.Funnel(name='Segunda repitencia', orientation='h',y = df_5['Área'],x = df_5['Segunda repitencia'],
                marker = {'color': ['indianred','indianred','indianred','indianred','indianred']}))

fig_5.add_trace(go.Funnel(name='Tercera repitencia', orientation='h',y = df_5['Área'],x = df_5['Tercera repitencia'],
                marker = {'color': ['teal','teal','teal','teal','teal']}))
st.plotly_chart(fig_5)

#----------------------------------------------------------------------------------------------------------
st.subheader('6. Porcentajes de créditos aprobados según Área Académica:')

@st.cache(allow_output_mutation=True)
def load_data_6(nrows):
    datos_6 = pd.read_csv('./data/PORCENTAJE_DE_CREDITOS_APROBADOS_POR_AREA.csv', nrows=nrows)
    datos_6.fillna(0, inplace=True)
    #datos_6 = datos_6.sort_values('Primera repitencia',ascending=False)
    return datos_6

df_load_state = st.text('Cargando data ...')
datos_6 = load_data_6(5)

if st.checkbox('Mostrar datos 6'):
    st.subheader('Datos 6')
    st.write(datos_6)

df_6 = pd.read_csv('./data/PORCENTAJE_DE_CREDITOS_APROBADOS_POR_AREA.csv')
#df_6.fillna(0, inplace=True)

fig_6 = px.line(df_6, x= 'Área Académica', y=df_6.columns[1:8], width=1100, height=550, markers=True,
                    color_discrete_sequence = px.colors.qualitative.Light24_r)
fig_6.update_layout(xaxis_title= 'Área Académica', yaxis_title='Cantidad de Porcentaje de Créditos Aprobados',
                        legend_title='Intervalos de Porcentaje')

st.plotly_chart(fig_6)
# --------------------------------------------------------------------------------------------------------

st.subheader('7. Top 10 de Facultades con mayor número de repitencias:')

###################################################################


# --------------------------------------------------------------------------------------------------------
st.subheader('8. Top 20 de cursos con mayor número de repitencias:')

#####################################################################
@st.cache(allow_output_mutation=True)
def load_data_8(nrows):
    datos_8 = pd.read_csv('./data/REPITENCIAS_POR_CURSO.csv', nrows=nrows)
    datos_8 = datos_8.sort_values(by="Total Repitencias",ascending=False)
    datos_8 = datos_8.reset_index(drop=True)
    return datos_8

df_load_state = st.text('Cargando data ...')
datos_8 = load_data_8(3356)

if st.checkbox('Mostrar datos 8'):
    st.subheader('Datos 8')
    st.write(datos_8)

#####################################################################

df_8 = pd.read_csv('./data/REPITENCIAS_POR_CURSO.csv')
df_8 = df_8.sort_values('Total Repitencias',ascending=False)
df_8 = df_8.reset_index(drop=True)
df_8 = df_8.head(20)

fig_8 = px.bar(df_8, y='Total Repitencias', x='Cursos',text_auto = True,
       orientation = 'v',color = 'Total Repitencias', color_continuous_scale = 'viridis')
fig_8.update_layout(width=1000, height=650)
fig_8.update_layout(xaxis_title= 'Cursos', yaxis_title='Cantidad de Repitencias',
                        legend_title='Cantidad de Repitencias')
fig_8.update_xaxes(tickangle=28) # tickfont=dict(color='black', size=11))
st.plotly_chart(fig_8)

# -------------------------------------------------------------------------------------

st.subheader('9. Estudiantes Invictos vs estudiantes con Repitencias:')

@st.cache(allow_output_mutation=True)
def load_data_9(nrows):
    datos_9 = pd.read_csv('./data/INVICTOS_VS_REPITENTES.csv', nrows=nrows)
    return datos_9

df_load_state = st.text('Cargando data ...')
datos_9 = load_data_9(20)

if st.checkbox('Mostrar datos 9'):
    st.subheader('Datos 9')
    st.write(datos_9)

df_9 = pd.read_csv('./data/INVICTOS_VS_REPITENTES.csv')

import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig_9 = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=False,
                    shared_yaxes=True, horizontal_spacing=0)

fig_9.append_trace(go.Bar(x=df_9['Repitentes'],
                     y    = df_9['Facultad'], 
                     text = df_9['Repitentes'].map('{:,.0f}'.format), #Display the numbers with thousands separators in hover-over tooltip 
                     textposition='inside',
                     orientation='h', 
                     width=0.7, 
                     showlegend=False, 
                     marker_color='cyan'), 
                     1, 1) # 1,1 represents row 1 column 1 in the plot grid

fig_9.append_trace(go.Bar(x = df_9['Invictos'],
                        y = df_9['Facultad'], 
                     text=df_9['Invictos'].map('{:,.0f}'.format),
                     textposition='inside',
                     orientation='h', 
                     width=0.7, 
                     showlegend=False, 
                     marker_color='DarkSlateGrey'), 
                     1, 2) # 1,2 represents row 1 column 2 in the plot grid

fig_9.update_xaxes(showticklabels=False, title_text='Repitentes', row=1, col=1, range=[2350,0])
fig_9.update_xaxes(showticklabels=False, title_text='Invictos', row=1, col=2 ,range=[0,2350])     

fig_9.update_layout(width=1100, height=650)
st.plotly_chart(fig_9)

### -------------------------------------------------------------------------------------

st.subheader('10. Estado de Permanencia de los estudiantes según años de estudio:')

df_10 = pd.read_csv('./data/PERMANENCIA_ANIO_INGRESO.csv')
df_10.fillna(0, inplace=True)
st.write(df_10)

