import streamlit as st
from modulos.login import login
from modulos.menu import mostrar_menu

# Verificar si la sesión ya está iniciada
if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:
    mostrar_menu()
else:
    login()
