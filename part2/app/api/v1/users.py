from flask_restx import Namespace, Resource, fields
from app.services import facade
from app.models.user import User
from cerberus import Validator
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user')
})

# user_response_model = api.model(
#     'UserResponse',
#     user_model.clone('UserResponse', {
#         'first_name': fields.String(required=True, description='First name of the user'),
#         'last_name': fields.String(required=True, description='Last name of the user')
#     }))

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload  
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400
        try:
            new_user = facade.create_user(user_data)
        except ValueError as e:
            return {"error": str(e)}, 400
        
        return {'id': new_user.id}, 201
    
    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        list_users = facade.list_users()
        return [{'id': list.id, 'first_name': list.first_name, 'last_name': list.last_name, 'email': list.email}
                for list in list_users], 200

@api.route('/<user_id>')
class UserResource(Resource):
    @jwt_required()
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200
    
    @jwt_required()
    @api.expect(user_model)
    @api.response(200, 'User updated successfully', user_model)
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    def put(self, user_id):
        current_user = get_jwt_identity()
        user_data = api.payload
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        print(current_user)
        if current_user['id'] == user.id:
            print("chau")
            #existing_user = facade.get_user_by_email(user_data['email'])
            #if existing_user:
            #    return {'error': 'email already exist'}, 400
            print("hola")
            if user_data['email'] != user.email:
                return {'error': 'Cannot modify email'}, 400
            print(user_data['password'])
            if user.verify_password(user_data['password']):
                return {'error': 'Cannot modify password'}, 400
            facade.update_user(user_id, user_data)
            print(user_data)
            return {'User updated'}, 200
        else:
            return {'error': 'Denied access'}, 400
