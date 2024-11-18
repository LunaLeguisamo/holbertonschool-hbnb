from . import BaseModel

class Amenity(BaseModel):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, string):
        if len(string) <= 50:
            self._name = string
        else:
            raise ValueError("Name is too long")
