from . import BaseModel
from app.models.place import Place
from app.models.user import User

class Review(BaseModel):
    def __init__(self, text: str, rating: int, place_id: Place, user_id: User):
        super().__init__()
        self.text = text
        if rating >= 1 and rating <= 5:
            self.rating = rating
        else:
            raise ValueError("Rating must be between 1 and 5")
        self.place_id = place_id
        self.user_id = user_id

    def __del__(self):
        return "Review deleted"