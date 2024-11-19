from . import BaseModel
from app.models.place import Place
from app.models.user import User

class Review(BaseModel):
    def __init__(self, text: str, rating: int, place_id: Place, user_id: User):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id
    
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, value):
        if value >= 1 and value <= 5:
            self._rating = value
        else:
            raise ValueError("Rating must be between 1 and 5")
    