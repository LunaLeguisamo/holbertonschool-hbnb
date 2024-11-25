import uuid
from datetime import datetime
from app import db

class BaseModel:
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    def __init__(self):
        __abstract__ = True # This ensures SQLAlchemy does not create a table for BaseModel
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        print({"data": data})
        for key, value in data.items():
            print(key, value)
            if hasattr(self, key):
                print("true")
                setattr(self, key, value)
        self.save()  # Update the updated_at timestamp