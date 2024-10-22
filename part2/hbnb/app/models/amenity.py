from . import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        if len(name) <= 50:
            self.name = name
        else:
            return "Name is too long"
  
    def delete_amenity(self):
        #eliminar amenity
        
        
    def list_amenities(self):
        #listar ameninties