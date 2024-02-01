from models.models import Model
import os
import re
from datetime import datetime
from config.server import create_connection, close_connection
from utils.validaciones import validate_photo, validate_nombre,  validate_description
class ModelContacts(Model):
    path= path = os.path.join(os.path.dirname(__file__), '../data/comments.json')
    table = "comments"
    def __init__(self, path=None):
        super().__init__(path if path else self.path)

    def create(self):
        while True:
            nombre = input('Introduce el nombre: ')
            if validate_nombre(nombre):
                break

        while True:
            foto_perfil = input('Introduce la URL de la foto: ')
            if validate_photo(foto_perfil):
                break

        fecha = datetime.now().strftime("%Y-%m-%d")
        archive = 0
        while True:
            comentario = input('Introduce la descripción: ')
            if validate_description(comentario):
                break
        
       
        connection = create_connection()
        if not connection:
            print("error: no se ha podido establecer la conexion")
            return
        try:
            query = f"INSERT INTO contacts (nombre ,fecha, foto_perfil, archive, comentario) VALUES (%s, %s, %s, %s, %s)"
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, (nombre ,fecha, foto_perfil, archive, comentario))

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
            id_contact = input('Introduce el id del contacto que deseas actualizar: ')
            query = f"SELECT * FROM contacts WHERE _id = '{id_contact}'"
            cursor.execute(query)
            data = cursor.fetchone()

            if data:
                break
            else:
                print(f"No se encontró el id {id_contact}. Inténtalo de nuevo.")

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
        update_query = f"UPDATE contacts SET {selected_column} = %s WHERE _id = %s"
        cursor.execute(update_query, (new_value, id_contact))
        connection.commit()
        print(f"Se actualizó la columna {selected_column} con el nuevo valor: {new_value} para el usuario con id {id_contact}")

        close_connection(connection)