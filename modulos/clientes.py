import streamlit as st
from config.conexion import obtener_conexion

def gestionar_clientes():
    st.header("📋 Gestión de Clientes")

    # Formulario para agregar cliente
    with st.form("form_cliente"):
        nombre = st.text_input("Nombre")
        email = st.text_input("Email")
        enviar = st.form_submit_button("Agregar Cliente")

        if enviar:
            if nombre.strip() == "" or email.strip() == "":
                st.warning("⚠️ Completa todos los campos.")
            else:
                try:
                    con = obtener_conexion()
                    cursor = con.cursor()
                    cursor.execute("INSERT INTO Clientes (Nombre, Email) VALUES (%s,%s)", (nombre,email))
                    con.commit()
                    st.success("Cliente agregado correctamente ✅")
                except Exception as e:
                    st.error(f"Error al registrar cliente: {e}")
                finally:
                    cursor.close()
                    con.close()

    # Mostrar tabla de clientes
    try:
        con = obtener_conexion()
        cursor = con.cursor()
        cursor.execute("SELECT Id_Cliente, Nombre, Email FROM Clientes")
        clientes = cursor.fetchall()
        st.subheader("Clientes registrados")
        for c in clientes:
            st.write(f"🆔 {c[0]} | {c[1]} | {c[2]}")
    finally:
        cursor.close()
        con.close()
