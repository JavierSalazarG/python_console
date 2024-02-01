import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

db_config = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
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