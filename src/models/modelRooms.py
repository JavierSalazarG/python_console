from models.models import Model
import os
from utils.validaciones import validate_photo, validate_nombre, validate_email, validate_description, validate_room_number,validate_rate ,validate_contact
from datetime import datetime
from config.server import create_connection, close_connection

class ModelRooms(Model):
    path= path = os.path.join(os.path.dirname(__file__), '../data/rooms.json')
    table = "rooms"
    def __init__(self, path=None):
        super().__init__(path if path else self.path)
    
    def create(self):
        bed_types = {
        1: "Individual",
        2: "Doble",
        3: "Queen",
        4: "King",
        
        }
        facilities = {
        1: "WiFi",
        2: "Secador de pelo",
        3: "TV",
        4: "Aire acondicionado",
        5: "Cafetera",
        6: "Servicio de habitaciones",
        7: "Jacuzzi",
        8: "Estacionamiento",
       
        }
        selected_facilities = []
        while True:
            imgs = input('Introduce la URL de la foto: ')
            if validate_photo(imgs):
                break
        while True:
            roomNumber = input('Introduce el numero de la habitación')
            if validate_room_number(roomNumber):
                break
        print("Selecciona el tipo de cama:")
        for number, bed_type in bed_types.items():
            print(f"{number}. {bed_type}")
        while True:
            try:
                selected_number_types = int(input("Ingresa el número correspondiente al tipo de cama: "))
                if selected_number_types in bed_types:
                
                    break
                else:
                    print("Error: Ingresa un número válido de la lista.")
            except ValueError:
                print("Error: Ingresa un número válido.")
                break
        
        print("Selecciona las facilidades (ingresa los números separados por comas):")
        for number, facility in facilities.items():
            print(f"{number}. {facility}")
        while True:
            try:
                selected_numbers = input("Ingresa los números correspondientes a las facilidades (separados por comas): ")
                selected_numbers = [int(number.strip()) for number in selected_numbers.split(",")]

                if all(number in facilities for number in selected_numbers):
                    selected_facilities = [facilities[number] for number in selected_numbers]
                    break
                else:
                    print("Error: Ingresa números válidos de la lista.")
            except ValueError:
                print("Error: Ingresa números válidos.")
                break
        while True:
            rate = input("Inserta el precio de la habitacion: ")
            if validate_rate(rate):
                break
        while True:
            offer = input("Tiene oferta? (si - no)")

            if offer == "si":
                offerPrice = input("Que porcentaje quieres de oferta")

            else:
                break
        while True:
            status = "Avalable"
            break
        
        while True:
            description = input("Quieres incluir un comentario?")
            if description == "si":
                description = True
                start_date = input("indica el comentario: ")
                break
            else:
                description = False
                break

        connection = create_connection()
        if not connection:
            print("error: no se ha podido establecer la conexion")
            return
        try:
            query = f"INSERT INTO rooms (imgs, roomNumber, bodTypes, facilities, rate, offerPrice, status, description, start_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, (imgs, roomNumber, selected_number_types, selected_facilities, rate, offerPrice, status, description, start_date))

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
            room_number = input('Introduce el numero de habitacion que deseas actualizar: ')
            query = f"SELECT * FROM rooms WHERE roomNumber = '{room_number}'"
            cursor.execute(query)
            data = cursor.fetchone()

            if data:
                break
            else:
                print(f"No se encontró el Numero {room_number}. Inténtalo de nuevo.")

        columns = list(data.keys())
        columns.remove('roomNumber')
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
        update_query = f"UPDATE rooms SET {selected_column} = %s WHERE roomNumber = %s"
        cursor.execute(update_query, (new_value, room_number))
        connection.commit()
        print(f"Se actualizó la columna {selected_column} con el nuevo valor: {new_value} para el usuario con correo {room_number}")

        close_connection(connection)