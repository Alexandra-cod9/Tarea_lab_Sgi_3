import streamlit as st
from modulos.login import login
from modulos.ventas import mostrar_venta      # tu venta simple original
from modulos.productos import mostrar_productos
from modulos.ventas import mostrar_ventas    # ventas con total y tabla nueva

# Inicializar sesión si no existe
if "sesion_iniciada" not in st.session_state:
    st.session_state["sesion_iniciada"] = False

# Comprobamos si la sesión ya está iniciada
if st.session_state["sesion_iniciada"]:
    # Mostrar menú lateral
    opciones = ["Ventas simples", "Productos", "Ventas con total"]  # Nuevas opciones
    seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

    # Mostrar módulo correspondiente
    if seleccion == "Ventas simples":
        mostrar_venta()
    elif seleccion == "Productos":
        mostrar_productos()
    elif seleccion == "Ventas con total":
        mostrar_ventas()
    else:
        st.write("Has seleccionado una opción no válida.")
else:
    # Si la sesión no está iniciada, mostrar login
    login()
