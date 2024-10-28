
# HBnB Evolution

## Description. 📋

HBnB Evolution is a property management application that allows users to add listings and amenities for others to rent and review. The architecture follows a layered design to enhance maintainability and scalability, with three main layers:

- **Presentation Layer**: The graphical interface that lets users interact and make API requests.
- **Business Logic Layer**: Manages core operations and data validation, including the main entities User, Place, Review, and Amenity.
- **Persistence Layer**: Stores, retrieves, and deletes information, interacting with the database through an ORM.

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
- [@Bryan Alemán](https://github.com/balemansteve)

