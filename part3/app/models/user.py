from . import BaseModel
from app import db
import re
from flask_bcrypt import Bcrypt
from app.models.__init__ import BaseModel
from sqlalchemy.orm import validates, relationship

bcrypt = Bcrypt()

class User(BaseModel, db.Model):
    __tablename__ = 'users'
    
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    places = relationship('Place', backref='user')
    reviews = relationship('Review', backref='user')
     
    def __init__(self, first_name:str, last_name:str, email:str, password:str, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.password = self.hash_password(password)
    
    @validates("first_name")
    def validate_first_name(self, key,string):
        if isinstance(string, str) and len(string) <= 50:
            return string
        else:
            raise ValueError("Name is too long")
    
    @validates("last_name")
    def validate_last_name(self, key, string):
        if len(string) <= 50 and isinstance(string, str):
            return string
        else:
            raise ValueError("Last name is too long")

    @validates("email")
    def validate_email(self, key, value):
        if self.validar_email(value) == True:
            return value
        else:
            raise ValueError("Invalid email")
    
    def validar_email(self, email):
        val = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(val, email):
            return True
        else:
            raise ValueError("Invalid email")

    def add_places(self, place):
        self.places.append(place)
        place.owner = self
    
    def get_user_list(self):
        return User.user_list
    
    def hash_password(self, password):
        """Hashes the password before storing it."""
        password = bcrypt.generate_password_hash(password).decode('utf-8')
        return password

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
