from . import BaseModel
from app.models.place import Place
from app.models.user import User

class Review(BaseModel):
    def __init__(self, text: str, rating: int, place:Place, user: User):
        super().__init__()
        self.text = text
        if rating >= 1 and rating <= 5:
            self.rating = rating
        else:
            raise ValueError("Error")
        if isinstance(place, Place):
            self.place = place
        else:
            raise ValueError("Error")
        if isinstance(user, User):
            self.user = user
        else:
            raise ValueError("Error")

    def __del__(self):
        #elmininar review
        return "Review deleted"