from app.persistence.UserRepository import UserRepository
from app.persistence.PlaceRepository import PlaceRepository
from app.persistence.AmenityRepository import AmenityRepository
from app.persistence.ReviewRepository import ReviewRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        self.place_repo = PlaceRepository()
        self.amenity_repo = AmenityRepository()
        self.review_repo = ReviewRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email)
    
    def list_users(self):
        list = self.user_repo.get_all()
        return list
    
    def update_user(self, user_id, user_data):
        update = self.user_repo.update(user_id, user_data)
        return update
    
    def create_amenity(self, amenity_data):
        amenity_name = amenity_data.get('name')
        new_amenity = Amenity(amenity_name)
        self.amenity_repo.add(new_amenity)
        return new_amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)


    def get_all_amenities(self):
        list_a = self.amenity_repo.get_all()
        return list_a

    def update_amenity(self, amenity_id, amenity_data):
        return self.amenity_repo.update(amenity_id, amenity_data)
    
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
        list_r = self.review_repo.get_all()
        return list_r

    def get_reviews_by_place(self, place_id):
        reviews = self.get_all_reviews()
        list = []
        for review in reviews:
            if review.place_id == place_id:
                list.append(review)
        return list
    
        #list_pr = self.review_repo.get_by_attribute("place_id", place_id)
        #return list_pr

    def update_review(self, review_id, review_data):
        update_p = self.review_repo.update(review_id, review_data)
        return update_p

    def delete_review(self, review_id):
        self.review_repo.delete(review_id)
        
    def delete_place(self, place_id):
        self.place_repo.delete(place_id)