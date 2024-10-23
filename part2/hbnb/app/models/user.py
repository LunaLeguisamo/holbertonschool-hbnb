from . import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin):
        super().__init__()
        if len(first_name) <= 50:
            self.first_name = first_name
        else:
            return "Name is too long"
        
        if len(last_name) <= 50:
            self.last_name = last_name
        else:
            return "Name is too long"

        self.email = email
        self.__is_admin = bool(is_admin)

    def __del__(self):
        return "User deleted"