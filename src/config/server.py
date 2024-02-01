import mysql.connector

db_config = {
    'host': 'localhost',
    'database': 'HotelMiranda',
    'user': 'root',
    'password': 'Root1999'
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

