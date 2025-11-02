import streamlit as st
from config.conexion import obtener_conexion

def mostrar_ventas():
    st.header("🛒 Registrar venta con producto")

    try:
        con = obtener_conexion()
        cursor = con.cursor()

        # Formulario para registrar venta
        with st.form("form_ventas"):
            producto = st.text_input("Nombre del producto")
            cantidad = st.number_input("Cantidad vendida", min_value=1, step=1)
            total = st.number_input("Total de la venta", min_value=0.0, step=0.01)
            enviar = st.form_submit_button("✅ Guardar venta")

            if enviar:
                if producto.strip() == "":
                    st.warning("⚠️ Debes ingresar el nombre del producto.")
                else:
                    try:
                        cursor.execute(
                            "INSERT INTO Ventas (Producto, Cantidad, Total) VALUES (%s, %s, %s)",
                            (producto, cantidad, total)
                        )
                        con.commit()
                        st.success(f"✅ Venta registrada: {producto} (Cantidad: {cantidad}, Total: ${total:.2f})")
                        st.rerun()
                    except Exception as e:
                        con.rollback()
                        st.error(f"❌ Error al registrar la venta: {e}")

    except Exception as e:
        st.error(f"❌ Error general: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals():
            con.close()

    # Mostrar todas las ventas registradas
    st.subheader("📋 Ventas registradas")
    try:
        con = obtener_conexion()
        cursor = con.cursor()
        cursor.execute("SELECT Id_Venta, Producto, Cantidad, total FROM Ventas")
        ventas = cursor.fetchall()

        if ventas:
            for venta in ventas:
                st.write(f"🆔 {venta[0]} | {venta[1]} — {venta[2]} unidades — Total: ${venta[3]:.2f}")
        else:
            st.info("Aún no hay ventas registradas.")
    except Exception as e:
        st.error(f"Error al mostrar ventas: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals():
            con.close()
