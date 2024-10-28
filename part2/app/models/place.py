from . import BaseModel
from app.models.user import User
class Place(BaseModel):
    places = []
    
    def __init__(self, title:str, description:str, price:float, latitude:float, longitude:float, owner):
        super().__init__()
        self._title = title
        self.description = description
        self._price = price
        self._latitude = latitude
        self._longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if value <= 100:
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
    
    @classmethod
    def add_place(cls, place):
        cls.places.append(place)
    
    def get_place_info(self):
        return {
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'owner': {
                'id': self.owner.id,
                'first_name': self.owner.first_name, 
                'last_name': self.last_name,
                'email': self.owner.email
                },
            'amenities': [{'id': amenity.id, 'name': amenity.name} for amenity in self.amenities],
            'reviews': self.reviews
        }

    def __del__(self):
        #eliminar place
        return "Place deleted"
