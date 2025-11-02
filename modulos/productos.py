import streamlit as st
from config.conexion import obtener_conexion

def mostrar_productos():
    st.header("📦 Registrar nuevo producto")

    try:
        con = obtener_conexion()
        cursor = con.cursor()

        # Formulario para registrar producto
        with st.form("form_producto"):
            nombre = st.text_input("Nombre del producto")
            precio = st.number_input("Precio", min_value=0.0, step=0.01)
            enviar = st.form_submit_button("✅ Guardar producto")

            if enviar:
                if nombre.strip() == "":
                    st.warning("⚠️ Debes ingresar el nombre del producto.")
                else:
                    try:
                        cursor.execute(
                            "INSERT INTO Productos (Nombre, Precio) VALUES (%s, %s)",
                            (nombre, precio)
                        )
                        con.commit()
                        st.success(f"✅ Producto registrado: {nombre} (Precio: {precio})")
                        st.rerun()
                    except Exception as e:
                        con.rollback()
                        st.error(f"❌ Error al registrar el producto: {e}")

    except Exception as e:
        st.error(f"❌ Error general: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals():
            con.close()

    # Mostrar todos los productos
    st.subheader("📋 Productos registrados")
    try:
        con = obtener_conexion()
        cursor = con.cursor()
        cursor.execute("SELECT Id_Producto, Nombre, Precio FROM Productos")
        productos = cursor.fetchall()

        if productos:
            for prod in productos:
                st.write(f"🆔 {prod[0]} | {prod[1]} — ${prod[2]:.2f}")
        else:
            st.info("Aún no hay productos registrados.")
    except Exception as e:
        st.error(f"Error al mostrar productos: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals():
            con.close()
