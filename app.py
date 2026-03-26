import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Mostrando un encabezado
st.header('Análisis de anuncios de ventas de coches en Estados Unidos')

# Mostrar un texto
st.text('Selecciona las gráficas que deseas visualizar y construye')

# Mostrando casillas de varificación
hist_checkbox = st.checkbox('Construir un histograma')
scatter_checkbox = st.checkbox('Construir un gráfico de dispersión')

# # Crear un botón en la aplicación Streamlit
# hist_button = st.button('Construir histograma')

# # Botón para mostrar un gráfico de dispersión
# scatter_button = st.button('Construir un gráfico de dispersión')

# Botón que crea las selecciones
primary_button = st.button('Construir')

if primary_button:
    # Lógica a ejecutar cuand se hace clic en el botón
    if hist_checkbox:
        # Escribir un mensaje en la aplicación
        st.write(
            'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

        # Crear un histograma utilizando plotply.graph_objects
        # Se crea una figura vacía y luego se añade un rastro de histograma
        fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

        # Título al gráfico
        fig.update_layout(title_text='Distribución del Odómetro')

        # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
        # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
        st.plotly_chart(fig, use_container_width=True)

    # Lógica a ejecutar cuando se hace clic en el botón
    if scatter_checkbox:
        # Escribir un mensaje en la aplicación
        st.write(
            'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

        # Crear el gráfico de dispersión
        fig = go.Figure(
            data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

        # Título al gráfico
        fig.update_layout(title_text='Relación entre Odómetro y Precio')

        # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
        # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
        st.plotly_chart(fig, use_container_width=True)
