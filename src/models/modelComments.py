from models.models import Model
import os
import re
from datetime import datetime
from config.server import create_connection, close_connection

class Comments(Model):
    path= path = os.path.join(os.path.dirname(__file__), '../data/comments.json')
    table = "comments"
    def __init__(self, path=None):
        super().__init__(path if path else self.path)

    def create(self):
        while True:
            photo = input('Introduce la URL de la foto: ')
            if self.validate_photo(photo):
                break

        while True:
            nombre = input('Introduce el nombre: ')
            if self.validate_nombre(nombre):
                break
        while True:
            email = input('Introduce el correo electrónico: ')
            if self.validate_email(email):
                break

        start_date = datetime.now().strftime("%Y-%m-%d")

        while True:
            description = input('Introduce la descripción: ')
            if self.validate_description(description):
                break
        while True:
            contact = input('Introduce el número de contacto: ')
            if self.validate_contact(contact):
                break
        status = input('Introduce el estado: ')

        data = {
            "photo": photo,
            "nombre": nombre,
            "email": email,
            "start_date": start_date,
            "description": description,
            "contact": contact,
            "status": status
        }
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