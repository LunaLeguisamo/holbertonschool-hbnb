from flask_restx import Namespace, Resource, fields, marshal
from app.services import facade
from cerberus import Validator
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

amenity_response_model = api.model(
    'AmenityResponse',
    amenity_model.clone('AmenityReponse', {"id": fields.String()})
)

@api.route('/')
class AmenityList(Resource):
    @jwt_required()
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        amenity_data = api.payload  
        current_user = get_jwt_identity()
        
        if not current_user['is_admin']:
            return {'error': 'Admin privileges required'}
        
        try:
            new_amenity = facade.create_amenity(amenity_data)
            return {'id': new_amenity.id, 'name': new_amenity.name}, 201
        except ValueError as e:
            return {"error": str(e)}, 400
        

    @api.response(200, 'List of amenities retrieved successfully', [amenity_response_model])
    def get(self):
        """Retrieve a list of all amenities"""
        list_amenities = facade.get_all_amenities()
        return marshal(list_amenities, amenity_response_model), 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @jwt_required()
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404
        return {'id': amenity.id, 'name': amenity.name}, 200

    @api.expect(amenity_model, validate=True)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, amenity_id):
        """Update an amenity's information"""
        current_user = get_jwt_identity()

        amenity_data = api.payload

        amenity = facade.get_amenity(amenity_id)

        if not amenity:
            return {'error': 'Amenity not found'}, 404

        if not current_user['is_admin']:
            return {'error': 'Admin privileges required'}

        print(amenity_data, amenity.id)
        update = facade.update_amenity(amenity.id, amenity_data)
        print(update)
        amenity = facade.get_amenity(amenity_id)
        print(amenity.name)

        return {"message": "Amenity updated successfully"}, 200
