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
    'password': fields.String(required=True, description='Password of the user'),
    'is_admin': fields.Boolean(required=True, description="Rol of the user")
})

user_response_model = api.model(
    'UserPutPayload',
    {'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user')}
)

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Register a new user"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        
        user_data = api.payload
        
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400
        try:
            new_user = facade.create_user(user_data)
        except ValueError as e:
            return {"error": str(e)}, 400
        
        return {'id': new_user.id, 'messagge': 'User successfully created'}, 201
    
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
        
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        
        user_data = api.payload
        
        user = facade.get_user(user_id)
        
        if not user:
            return {'error': 'User not found'}, 404
        
        print(current_user)
        
        if current_user['id'] != user.id:
            return {'error': 'Denied access'}, 400
        
        email = user_data.get('email')
        password = user_data.get('password')
        
        if email:
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'email is already in use'}, 400
        
        if password:
            new_password = User.hash_password(password)
            user_data['password'] = new_password
        
        # if "email" in user_data:
        #     return {'error': 'Cannot modify email'}, 400

        # if "password" in user_data:
        #     return {'error': 'Cannot modify password'}, 400

        # correct_data = {
        #     "first_name": user_data.get("first_name"),
        #     "last_name": user_data.get("last_name")
        # }

        # facade.update_user(user_id, correct_data)
        facade.update_user(user_id, user_model)
        print(user_data)
        print("xd")
        return {'id': user.id,'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200
    
