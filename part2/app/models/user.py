from . import BaseModel
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(BaseModel):
    user_list = []
    
    def __init__(self, first_name:str, last_name:str, email:str, password:str, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []
        self.password = password
        User.user_list.append(self) 
        
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, string):
        if len(string) <= 50 and isinstance(string, str):
            self._first_name = string
        else:
            raise ValueError("Name is too long")
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, string):
        if len(string) <= 50 and isinstance(string, str):
            self._last_name = string
        else:
            raise ValueError("Last name is too long")

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not self.validar_email(value):
            raise ValueError("Invalid email")
        self._email = value
        
    def validar_email(self, email):
        val = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(val, email):
            raise ValueError("Invalid email")
        return True
        
    def add_places(self, place):
        self.places.append(place)
        place.owner = self
    
    def get_user_list(self):
        return User.user_list
