from flask_restx import Namespace, Resource, fields, marshal
from app.services import facade
from cerberus import Validator

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
})

# facade = HBnBFacade()

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
        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        # if user_data['email'] == None:
        #     return {'error': 'Invalid email'}, 400
        # else:
            
        # new_user = facade.create_user(user_data)
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201
    
    def get(self):
        list_users = facade.list_users()
        return marshal(list_users, user_model), 200

@api.route('/<user_id>')
class UserResource(Resource):
    @api.expect(user_model, validate=True)
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200
    
    def put(self, user_id):
        scheme = {
            'first_name': {'type': 'string'},
            'last_name': {'type': 'string'},
            'email': {'type': 'string', 'regex': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'}
        }
        
        val = Validator(scheme)
        user_data = api.payload
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        elif val.validate(user_data):
            facade.update_user(user_id, user_data)
            return "User updated", 200
        else:
            return "Invalidate data", 400