from app import create_app
from app.services import facade
from app.models.amenity import Amenity
from app.models.user import User

app = create_app()

facade.amenity_repo.add(Amenity("wifi"))
facade.amenity_repo.add(Amenity("pool"))
user =  User("admin", "admin", "admin@hbnb.com", True)
print(user.id)
facade.user_repo.add(user)

if __name__ == '__main__':
    app.run(debug=True)