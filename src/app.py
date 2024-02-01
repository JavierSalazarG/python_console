import argparse
from models.modelUser import ModelUserer  # Asegúrate de importar la clase correcta

def runApp():
    parser = argparse.ArgumentParser(
        prog="Python app",
        description="Datos de JSON")
    parser.add_argument("action", choices=['list_users', "view_users","delete_users", "create_users", "view_bookings", "list_bookings", "delete_bookings" "list_rooms" , "view_rooms","delete_rooms", "list_comments", "view_comments", "delete_comments", "create_comments", "update_comments"])
    
    argumentos = parser.parse_args()

    # Crear una instancia de ModelUserer
    user_model = ModelUserer()

    if argumentos.action == 'list_users':
        user_model.list()
    elif argumentos.action == 'view_users':
        user_model.view()
    elif argumentos.action == 'delete_users':
        user_model.delete()
    elif argumentos.action == "create_users":
        user_model.create()
    elif argumentos.action == 'list_bookings':
        Bookings.list()
    elif argumentos.action == 'view_bookings':
        Bookings.view()
    elif argumentos.action == 'delete_bookings':
        Bookings.delete()
    elif argumentos.action == 'list_rooms':
        Rooms.list()
    elif argumentos.action == 'delete_rooms':
        Rooms.delete()
    elif argumentos.action == 'view_rooms':
        Rooms.view()
    elif argumentos.action == 'list_comments':
        Comments.list()
    elif argumentos.action == 'view_comments':
        Comments.view()
    elif argumentos.action == 'delete_comments':
        Comments.delete()
    elif argumentos.action == "create_comments":
        
        datas = {
                "nombre": input("introduce tu nombre:"),
                "foto_perfil": "https://loremflickr.com/cache/resized/65535_52630952123_7666ab4252_b_640_480_nofilter.jpg",
                "comentario": input("escribe tu comentario:"),
                "archive": False
            }
        Comments.create(datas)
    elif argumentos.action == "update_comments":
        Comments.update()
runApp()