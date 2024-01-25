from abc import ABC, abstractmethod
from datetime import datetime
import json

class Model(ABC):
    def __init__(self, path):
        self.path = path
    @classmethod
    def list(cls):
        with open(cls.path) as json:
            readJson = json.red()
            print(readJson)