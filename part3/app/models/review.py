from . import BaseModel
from app.models.place import Place
from app.models.user import User
from app import db
from sqlalchemy.orm import validates


class Review(BaseModel, db.Model):
    __tablename__ = 'reviews'

    text = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    place_id = db.Column(db.String(50),  db.ForeignKey("places.id"),nullable=False)
    user_id = db.Column(db.String(50), db.ForeignKey("users.id"),nullable = False, unique=True)

    def __init__(self, text: str, rating: int, place_id: Place, user_id: User):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id
    
    
    @validates("rating")
    def validate_rating(self, key, value):
        if value >= 1 and value <= 5:
            self.rating = value
        else:
            raise ValueError("Rating must be between 1 and 5")
    