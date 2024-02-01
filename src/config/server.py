import mysql.connector
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'HotelMiranda'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'Root1999')
}

def create_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        print("Conexión exitosa:", connection)
        return connection
    except mysql.connector.Error as err:
        print("Error de conexión:", err)
        return None

def close_connection(connection):
    if connection:
        connection.close()
        print("Conexión cerrada")