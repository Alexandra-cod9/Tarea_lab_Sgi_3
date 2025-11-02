import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='bgdcfmb1arijnmihxnub-mysql.services.clever-cloud.com',
            user='up0crtddmf4aoous',
            password='mkHalSz2YPOtR8jya8DS',
            database='bgdcfmb1arijnmihxnub',
            port=3306
        )
        if conexion.is_connected():
            return conexion
        else:
            return None
    except Error as e:
        print(f"Error al conectar: {e}")
        return None
