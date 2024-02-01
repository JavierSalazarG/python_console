from abc import ABC, abstractmethod
from datetime import datetime
import json
import os
from config.server import create_connection, close_connection
class Model(ABC):
    
    def __init__(self, path):
        self.path = path
        self.table = None
    @classmethod
    def list(cls):
        connection = create_connection()
        if not connection:
            return None

        cursor = connection.cursor(dictionary=True)
        query = f"SELECT * FROM {cls.table}"
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            print(results) 
        except mysql.connector.Error as err:
            print(f"Error de ejecución de la consulta: {err}")
            results = None
        finally:
            cursor.close()
            close_connection(connection)
        
        return results
        
    @classmethod
    def view(cls):
        connection = create_connection()
        if not connection:
            return None

        try:
            cursor = connection.cursor(dictionary=True)
            find_id = input('Introduce el ID: ')

            query = f"SELECT * FROM {cls.table} WHERE _id = {find_id}"
            cursor.execute(query)
            data = cursor.fetchall()
            print(data)
            
        except mysql.connector.Error as err:
            print(f"Error durante la conexión o ejecución de la consulta: {err}")
            data = None
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            close_connection(connection)

        return data
    @classmethod
    def delete(cls):
        connection = create_connection()
        if not connection:
            return None

        try:
            cursor = connection.cursor(dictionary=True)
            find_id = input('Introduce el ID que desea eliminar: ')

            query = f"DELETE * FROM {cls.table} WHERE _id = {find_id}"
            cursor.execute(query)
            data = cursor.fetchall()
            print(data)
            
        except mysql.connector.Error as err:
            print(f"Error durante la conexión o ejecución de la consulta: {err}")
            data = None
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            close_connection(connection)

        return data

    @classmethod
    def create():
        pass

    @classmethod
    def update():
        pass
            

class Users(Model):
    
    table = "users"
class Comments(Model):
    path= path = os.path.join(os.path.dirname(__file__), '../data/comments.json')
    table = "comments"

class Rooms(Model):
    path= path = os.path.join(os.path.dirname(__file__), '../data/rooms.json')
    table = "rooms"
class Bookings(Model):
    path= path = os.path.join(os.path.dirname(__file__), '../data/bookings.json')
    table = "bookings"