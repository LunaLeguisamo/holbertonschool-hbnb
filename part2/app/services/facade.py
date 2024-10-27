from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    def list_users(self):
        list = self.user_repo.get_all()
        return list
    
    def update_user(self, user_id, user_data):
        update = self.user_repo.update(user_id, user_data)
        return update
    
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)


    def get_all_amenities(self):
        list_a = self.amenity_repo.get_all()
        return list_a

    def update_amenity(self, amenity_id, amenity_data):
        update_a = self.amenity_repo.update(amenity_id, amenity_data)
        return update_a
    
    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)


    def get_all_places(self):
        list_p = self.place_repo.get_all()
        return list_p

    def update_place(self, place_id, place_data):
        update_p = self.place_repo.update(place_id, place_data)
        return update_p
    
    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        list_r + self.review_repo.get_all()
        return list_r

    def get_reviews_by_place(self, place_id):
        

    def update_review(self, review_id, review_data):
        update_p = self.review_repo.update(review_id, review_data)
        return update_p

    def delete_review(self, review_id):
        # Placeholder for logic to delete a review
        pass