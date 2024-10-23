from . import BaseModel

class Amenity(BaseModel):
    def __init__(self, name=str):
        super().__init__()
        if len(name) <= 50:
            self.name = name
        else:
            return "Name is too long"
  
    def __del__(self):
        #eliminar amenity
        return "Amenity deleted"
