import streamlit as st
from modulos.clientes import gestionar_clientes
from modulos.productos import gestionar_productos
from modulos.ventas import gestionar_ventas

def mostrar_menu():
    opciones = ["Clientes", "Productos", "Ventas"]
    seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

    if seleccion == "Clientes":
        gestionar_clientes()
    elif seleccion == "Productos":
        gestionar_productos()
    elif seleccion == "Ventas":
        gestionar_ventas()
