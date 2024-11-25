from . import BaseModel
from app import db
from sqlalchemy.orm import validates

class Amenity(BaseModel, db.Model):
    __tablename__ = 'amenities'

    name = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    @validates("name")
    def validates_name(self, string):
        if len(string) <= 50:
            self.name = string
        else:
            raise ValueError("Name is too long")
