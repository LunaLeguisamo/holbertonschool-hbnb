from . import BaseModel
import re

class User(BaseModel):
    def __init__(self, first_name=str, last_name=str, email=str, is_admin=False):
        super().__init__()
        if len(first_name) <= 50:
            self.first_name = first_name
        else:
            return "Name is too long"
        
        if len(last_name) <= 50:
            self.last_name = last_name
        else:
            return "Name is too long"
        self.is_admin = is_admin
        self.email = email
        self.places = []

    def validar_email(email):
        # Expresión regular para validar el formato del correo electrónico
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        # Comprobar si el email coincide con el patrón
        if re.match(regex, email):
            return True
        else:
            return False
    
    def add_places(self, place):
        self.places.append(place)
    
    def __del__(self):
        return "User deleted"