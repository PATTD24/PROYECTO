import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV en un DataFrame
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de datos de anuncios de venta de coches')

# Casilla de verificación para construir un histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    # Mostrar mensaje
    st.write('Construyendo un histograma para la columna odómetro')
    
    # Crear el histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar el gráfico de Plotly
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    # Mostrar mensaje
    st.write('Construyendo un gráfico de dispersión para la columna odómetro y precio')
    
    # Crear el gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # Mostrar el gráfico de Plotly
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para construir un gráfico de pastel
build_pie_chart = st.checkbox('Construir un gráfico de pastel para la distribución de la condición del automóvil')

if build_pie_chart:
    # Mostrar mensaje
    st.write('Construyendo un gráfico de pastel para la distribución de la condición del automóvil')
    
    # Contar valores de la condición del automóvil
    condition_counts = car_data['condition'].value_counts()
    
    # Crear el gráfico de pastel
    fig = px.pie(values=condition_counts, names=condition_counts.index)
    
    # Mostrar el gráfico de Plotly
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para construir un gráfico de barras
build_bar_chart = st.checkbox('Construir un gráfico de barras para la distribución del modelo de automóvil')

if build_bar_chart:
    # Mostrar mensaje
    st.write('Construyendo un gráfico de barras para la distribución del modelo de automóvil')
    
    # Contar valores del modelo de automóvil
    model_counts = car_data['model'].value_counts().head(10)  # Tomar los 10 modelos más comunes
    
    # Crear el gráfico de barras
    fig = px.bar(x=model_counts.index, y=model_counts.values)
    
    # Configurar etiquetas y título
    fig.update_layout(xaxis_title='Modelo de Automóvil', yaxis_title='Cantidad', title='Distribución del Modelo de Automóvil')
    
    # Mostrar el gráfico de Plotly
    st.plotly_chart(fig, use_container_width=True)
