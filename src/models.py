from abc import ABC, abstractmethod
from datetime import datetime
import json
import os
class Model(ABC):
    def __init__(self, path):
        self.path = path
    @classmethod
    def list(cls):
        with open(cls.path, encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                print(item)
                print()
    @classmethod
    def view(cls):
        with open(cls.path) as file:
            data = json.load(file)
            print('Introduce id')
            id = input()
        for element in data:
            if element["_id"] == int(id):
                print(element)
    @classmethod
    def delete(cls):
        with open(cls.path, 'r') as file:
            data = json.load(file)
        print('Introduce id para eliminar:')
        id = int(input())
        elements = [element for element in data if element['_id'] != id]
        if any(element["_id"] == id for element in data):
            print(f"el id {id} se ha eliminado correctamente")
        else:
            print('id no encontrado')
        for element in elements:
            print(element)

    @classmethod
    def create(cls):
        with open(cls.path) as file:
            data = json.load(file)
            l_data = len(data)

            fecha = datetime.now()
            new_comments = {
                "_id": l_data + 1,
                "nombre": input("introduce tu nombre:"),
                "fecha": fecha,
                "foto_perfil": "https://loremflickr.com/cache/resized/65535_52630952123_7666ab4252_b_640_480_nofilter.jpg",
                "comentario": input("escribe tu comentario:"),
                "archive": False
            }
            respuesta_archive = input("¿Deseas archivar el comentario? (responde 'si' o 'no'): ").lower()

            if respuesta_archive == 'si':
                new_comments["archive"] = True

            print("se a creado con exito el comentario!")
            print(new_comments)

    @classmethod
    def update(cls):
         with open(cls.path) as file:
            data = json.load(file)
            print('Introduce id')
            id = int(input())

            for comment in data:
                if comment["_id"] == id:
                    print("comentario elegido:")
                    print(comment)

                    respuesta_actualizar = input("¿Deseas actualizar el comentario? (responde 'si' o 'no'): ").lower()

                    if respuesta_actualizar == 'si':
                        comment["nombre"] = input("introduce el Nombre nuevo")
                        comment["comentario"] = input("introduce el comentario Nuevo ")
                        print("Comentario actualizado:")
                        print(comment)
                    else:
                        print("Comentario no actualizado")
                    return
                print(f"el comentario con el id {id} no se ha encontrado")

            

class Users(Model):
    path = os.path.join(os.path.dirname(__file__), '../data/user.json')

class Comments(Model):
    path= path = os.path.join(os.path.dirname(__file__), '../data/comments.json')

class Rooms(Model):
    path= path = os.path.join(os.path.dirname(__file__), '../data/rooms.json')

class Bookings(Model):
    path= path = os.path.join(os.path.dirname(__file__), '../data/bookings.json')