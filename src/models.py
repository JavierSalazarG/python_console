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
    

class Users(Model):
    path = os.path.join(os.path.dirname(__file__), '../data/user.json')

class Comments(Model):
    path= path = os.path.join(os.path.dirname(__file__), '../data/comments.json')

class Rooms(Model):
    path= path = os.path.join(os.path.dirname(__file__), '../data/rooms.json')

class Bookings(Model):
    path= path = os.path.join(os.path.dirname(__file__), '../data/bookings.json')