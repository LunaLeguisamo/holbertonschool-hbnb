from . import BaseModel
from app.models.user import User
class Place(BaseModel):
    def __init__(self, title:str, description:str, price:float, latitude:float, longitude:float, owner_id: User):
        super().__init__()
        if len(title) <= 100:
            self.title = title
        else:
            return "Title is too long"
        self.description = description
        self.price = abs(price)
        if latitude >= -90 and latitude <= 90:
            self.latitude = latitude
        else:
            raise ValueError("Latitude is out of range")
        if longitude >= -180 and longitude <= 180:
            self.longitude = longitude
        else:
            raise ValueError("Longitude is out of range")
        self.owner_id = owner_id
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def __del__(self):
        #eliminar place
        return "Place deleted"
