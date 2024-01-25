import argparse
from models import Users, Comments, Rooms, Bookings

def runApp():
    parser = argparse.ArgumentParser(
        prog="Python app",
        description="Datos de JSON")
    parser.add_argument("action", choices=['list_users', "view_users", "view_bookings", "list_bookings", "list_rooms" , "view_rooms", "list_comments", "view_comments"])
    
    argumentos = parser.parse_args()

    if argumentos.action == 'list_users':
        Users.list()
    elif argumentos.action == 'view_users':
        Users.view()
    elif argumentos.action == 'list_bookings':
        Bookings.list()
    elif argumentos.action == 'view_bookings':
        Bookings.view()
    elif argumentos.action == 'list_rooms':
        Rooms.list()
    elif argumentos.action == 'view_rooms':
        Rooms.view()
    elif argumentos.action == 'list_comments':
        Comments.list()
    elif argumentos.action == 'view_comments':
        Comments.view()
runApp()