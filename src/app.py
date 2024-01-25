import argparse
from models import Users, Comments, Rooms, Bookings

def runApp():
    parser = argparse.ArgumentParser(
        prog="Python app",
        description="Datos de JSON")
    parser.add_argument("action", choices=['list_users', "list_bookings", "list_rooms", "list_comments"])
    
    argumentos = parser.parse_args()

    if argumentos.action == 'list_users':
        Users.list()
    elif argumentos.action == 'list_bookings':
        Bookings.list()
    elif argumentos.action == 'list_rooms':
        Rooms.list()
    elif argumentos.action == 'list_comments':
        Comments.list()
runApp()