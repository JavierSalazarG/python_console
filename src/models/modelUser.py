from models.models import Model
import os
from utils.validaciones import validate_photo, validate_nombre, validate_email, validate_description, validate_contact
from datetime import datetime
from config.server import create_connection, close_connection
class ModelUser(Model):
    table = "users"
    path = os.path.join(os.path.dirname(__file__), '../data/user.json')
    def __init__(self, path=None):
        super().__init__(path if path else self.path)
    
    def create(self):

        while True:
            photo = input('Introduce la URL de la foto: ')
            if validate_photo(photo):
                break

        while True:
            nombre = input('Introduce el nombre: ')
            if validate_nombre(nombre):
                break
        while True:
            email = input('Introduce el correo electrónico: ')
            if validate_email(email):
                break

        start_date = datetime.now().strftime("%Y-%m-%d")

        while True:
            description = input('Introduce la descripción: ')
            if validate_description(description):
                break
        while True:
            contact = input('Introduce el número de contacto: ')
            if validate_contact(contact):
                break
        status = input('Introduce el estado: ')

    
        connection = create_connection()
        if not connection:
            print("error: no se ha podido establecer la conexion")
            return
        try:
            query = f"INSERT INTO users (photo, nombre, email, start_date, description, contact, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, (photo, nombre, email, start_date, description, contact, status))

            connection.commit()
            
            print("Datos ingresados correctamente.")
        
        except Exception as e:
            print(f"Error durante la inserción de datos: {e}")
        
        finally:
          
            close_connection(connection)

    def update(self):
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        
        while True:
            email_user = input('Introduce el correo del usuario que deseas actualizar: ')
            query = f"SELECT * FROM users WHERE email = '{email_user}'"
            cursor.execute(query)
            data = cursor.fetchone()

            if data:
                break
            else:
                print(f"No se encontró el correo {email_user}. Inténtalo de nuevo.")

        columns = list(data.keys())
        columns.remove('email')
        print("Selecciona la columna que deseas actualizar:")
        for i, column in enumerate(columns, start=1):
            print(f"{i}. {column}")

        while True:
            try:
                selected_column_number = int(input("Ingresa el número correspondiente a la columna que deseas actualizar: "))
                selected_column = columns[selected_column_number - 1]
                break
            except (ValueError, IndexError):
                print("Error: Ingresa un número válido de la lista.")

        new_value = input(f'Introduce el nuevo valor para {selected_column}: ')
        update_query = f"UPDATE users SET {selected_column} = %s WHERE email = %s"
        cursor.execute(update_query, (new_value, email_user))
        connection.commit()
        print(f"Se actualizó la columna {selected_column} con el nuevo valor: {new_value} para el usuario con correo {email_user}")

        close_connection(connection)