from . import BaseModel
from app.models.user import User
class Place(BaseModel):
    places = []
    
    def __init__(self, title:str, description:str, price:float, latitude:float, longitude:float, owner, amenities=None):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        if amenities is None:
            self.amenities = []  # List to store related amenities
        else:
            self.amenities = amenities
        self.reviews = []  # List to store related reviews
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if len(value) <= 100:
            self._title = value
        else:
            raise ValueError("Title is too long")
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise ValueError("Invalid type value")
        else:
            self._price = abs(value)
    
    @property
    def latitude(self):
        return self._latitude
    
    @latitude.setter
    def latitude(self, value):
        if value >= -90 and value <= 90:
            self._latitude = value
        else:
            raise ValueError("Latitude is out of range")
    @property
    def longitude(self):
        return self._longitude
    
    @longitude.setter
    def longitude(self, value):
        if value >= -180 and value <= 180:
            self._longitude = value
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

