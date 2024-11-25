
# 🏠 HBnB Evolution

## Description. 📋

HBnB Evolution is a property management application that allows users to add listings and amenities for others to rent and review. The architecture follows a layered design to enhance maintainability and scalability, with three main layers:

- **Presentation Layer**: The graphical interface that lets users interact and make API requests.
- **Business Logic Layer**: Manages core operations and data validation, including the main entities User, Place, Review, and Amenity.
- **Persistence Layer**: Stores, retrieves, and deletes information, interacting with the database through an ORM.

## Entity Models in Business Logic Layer ##

### Users 
- Represent the users of the application, who can be `owners` of places. Users have attributes.  
- Attributes: `first name`, `last name`, `email` and `id`  
### Places  
- These are the places created by users (owners). Each place can also have amenities.
- Attributes: `title`, `description`, `price`, `latitude`, `longitude`, `id`, `owner id` and `amenities`  
### Amenities
- These are the features or facilities that a place may offer, such as "Wi-Fi" or "Parking".
- In the model, a place can have multiple amenities.
- Attributes: `name` and `id`  
### Reviews
- These are the reviews of places, it's associated with a specific place and a specific user who wrote it.
- Attributes: `text`, `rating`, `place id` and `user id`

## Relationship ##

- Users can own Places (one-to-many relationship).  
- Places can have multiple Amenities and multiple Reviews.  
- Amenities can belong to multiple Places (many-to-many relationship).  
- Reviews are associated with both a User and a Place (many-to-one relationship with each).


## Setup and Installation ⚙️ 

### 1. Clone the repository

```bash
  git clone https://github.com/username/hbnb.git
  cd hbnb
```

### 2. Create and activate a virtual environment (optional):

```bash
  python3 -m venv venv
  source venv/bin/activate
```

### 3. Install dependencies

```bash
  pip install -r requirements.txt
```

### 4. Running the Application
#### Run the following command to start the application in development mode:

```bash
  python run.py
```
#### Access the API at http://localhost:5000/

## Authors 👥

- [@Luna Leguisamo](https://github.com/LunaLeguisamo)
- [@Julieta Bobadilla](https://github.com/)

