from . import BaseModel
from app import db
from sqlalchemy.orm import validates, relationship

place_amenity = db.Table('place_amenity',
db.Column('place_id', db.Integer, db.ForeignKey('places.id'), primary_key=True),
db.Column('amenity_id', db.Integer, db.ForeignKey('amenities.id'), primary_key=True))

class Place(BaseModel, db.Model):
    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitute = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    reviews = relationship('Review', backref='places')
    amenities = relationship('Amenity', secondary=place_amenity,
                           backref= db.backref('places'))
    
    def __init__(self, title:str, description:str, price:float, latitude:float, longitude:float, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner  
    
    @validates("title")
    def validates_title(self, key, value):
        if len(value) <= 100:
            self.title = value
        else:
            raise ValueError("Title is too long")
    
    @validates("price")
    def validates_price(self, key, value):
        if not isinstance(value, float):
            raise ValueError("Invalid type value")
        else:
            self._price = abs(value)
    
    @validates("latitude")
    def validates_latitude(self, key, value):
        if value >= -90 and value <= 90:
            self.latitude = value
        else:
            raise ValueError("Latitude is out of range")
    
    @validates("longitude")
    def validates_longitude(self, key, value):
        if value >= -180 and value <= 180:
            self.longitude = value
        else:
            raise ValueError("Longitude out of range")
        
    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
    
    def get_amenities(self):
        return self.amenities
        
    @classmethod
    def add_place(cls, place):
        cls.places.append(place)

