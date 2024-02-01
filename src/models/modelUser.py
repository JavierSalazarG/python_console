from models.models import Model
import os
import re
from datetime import datetime
from config.server import create_connection, close_connection
class ModelUserer(Model):
    table = "users"
    path = os.path.join(os.path.dirname(__file__), '../data/user.json')
    def __init__(self, path=None):
        super().__init__(path if path else self.path)
    def validate_photo(self, photo):
        if not photo:
            print("Error: La URL de la foto no puede estar vacía.")
            return False
        return True
    def validate_nombre(self, nombre):
        
        if not re.match("^[a-zA-Z\s]+$", nombre):
            print("Error: El nombre solo puede contener letras y espacios.")
            return False
        return True
    
    def validate_email(self, email):
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            print("Error: Formato de correo electrónico inválido.")
            return False
        return True
    
    def validate_description(self, description):
        if len(description) < 5:
            print("Error: La descripción debe tener al menos 5 letras.")
            return False
        elif len(description) > 255:
            print("Error: La descripción no puede tener más de 255 letras.")
            return False
        return True
    
    def validate_contact(self, contact):
        if not re.match("^\d{9,12}$", contact):
            print("Error: El número de contacto debe tener entre 9 y 12 dígitos.")
            return False
        return True

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