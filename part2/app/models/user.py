from . import BaseModel
import re

class User(BaseModel):
    user_list = []
    
    def __init__(self, first_name:str, last_name:str, email:str, is_admin=False):
        super().__init__()
        self._first_name = first_name
        self._last_name = last_name
        self.is_admin = is_admin
        self._email = email
        self.places = []
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
        if self.validar_email(value) == True:
            self._email = value
        else:
            raise ValueError("Invalid email")
    
    def validar_email(self, email):
        val = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(val, email):
            return True
        else:
            return False
    
    def add_places(self, place):
        self.places.append(place)
        place.owner = self
    
    def get_user_list(self):
        return User.user_list
 
    def __del__(self):
        return "User deleted"