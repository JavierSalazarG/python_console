import argparse
from models.modelUser import ModelUser 
from models.modelContacts import ModelContacts
from models.modelRooms import ModelRooms
def runApp():
    parser = argparse.ArgumentParser(
        prog="Python app",
        description="Datos de JSON")
    parser.add_argument("action", choices=[
        'list_users', 
        "view_users",
        "delete_users", 
        "create_users", 
        
        "view_bookings", 
        "list_bookings", 
        "delete_bookings",

        "list_rooms" ,
        "view_rooms",
        "delete_rooms", 
        "create_rooms",


        "list_contacts", 
        "view_contacts", 
        "delete_contacts", 
        "create_contacts", 
        "update_contacts"])
    
    argumentos = parser.parse_args()

    user_model = ModelUser()
    contact_model = ModelContacts()
    rooms_model = ModelRooms()

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
        rooms_model.list()
    elif argumentos.action == 'view_rooms':
        rooms_model.view()
    elif argumentos.action == 'delete_rooms':
        rooms_model.delete()
    elif argumentos.action == 'create_rooms':
        rooms_model.create()


    elif argumentos.action == 'list_contacts':
        contact_model.list()
    elif argumentos.action == 'view_contacts':
        contact_model.view()
    elif argumentos.action == 'delete_contacts':
        contact_model.delete()
    elif argumentos.action == "create_contacts":
        contact_model.create()
    elif argumentos.action == "update_contacts":
        contact_model.update()
runApp()