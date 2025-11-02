import streamlit as st
from config.conexion import obtener_conexion

def verificar_usuario(usuario, contrasena):
    con = obtener_conexion()
    if not con:
        st.error("⚠️ No se pudo conectar a la base de datos.")
        return None
    try:
        cursor = con.cursor()
        query = "SELECT Usuario, Contra FROM USUARIO WHERE Usuario=%s AND Contra=%s"
        cursor.execute(query, (usuario, contrasena))
        result = cursor.fetchone()
        return result
    finally:
        cursor.close()
        con.close()

def login():
    st.title("Inicio de sesión")

    usuario = st.text_input("Usuario")
    contrasena = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        validacion = verificar_usuario(usuario, contrasena)
        if validacion:
            st.session_state["usuario"] = usuario
            st.session_state["sesion_iniciada"] = True
            st.success(f"Bienvenido {usuario} 👋")
            st.rerun()
        else:
            st.error("❌ Credenciales incorrectas.")
