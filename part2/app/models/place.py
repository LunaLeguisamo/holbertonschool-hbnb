from . import BaseModel
from app.models.user import User
class Place(BaseModel):
    def __init__(self, title:str, description:str, price:float, latitude:float, longitude:float, owner):
        super().__init__()
        if len(title) <= 100:
            self.title = title
        else:
            raise ValueError("Title is too long")
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities
        
    @property
    def price(self):
        return self.price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise ValueError("Invalid type value")
        else:
            self.price = abs(value)
    
    @property
    def latitude(self):
        return self.latitude
    
    @latitude.setter
    def latitude(self, value):
        if value >= -90 and value <= 90:
            return self.latitude == value
        else:
            raise ValueError("Latitude is out of range")
    @property
    def longitude(self):
        return self.longitude
    
    @longitude.setter
    def longitude(self, value):
        if value >= -180 and value <= 180:
            return self.longitude == value
        else:
            raise ValueError("Longitude out of range")
        
    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def __del__(self):
        #eliminar place
        return "Place deleted"
