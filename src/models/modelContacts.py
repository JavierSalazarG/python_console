from models.models import Model
import os
import re
from datetime import datetime
from config.server import create_connection, close_connection
from utils.validaciones import validate_photo, validate_nombre, validate_email, validate_description, validate_contact
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
        
        

        data = {
            "nombre": nombre,
            "foto_perfil": foto_perfil,
            "fecha": fecha,
            "comentario": comentario,
            "archive": archive
        }
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