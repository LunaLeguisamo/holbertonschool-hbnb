from flask_restx import Namespace, Resource, fields, marshal
from app.services import facade
from cerberus import Validator
from flask_jwt_extended import jwt_required, get_jwt_identity


api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @jwt_required()
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        review_data = api.payload
        place_id = review_data['place_id']
        place_data = facade.get_place(place_id)
        current_user = get_jwt_identity()
        
        list_review =  facade.get_reviews_by_place(review_data['id'], place_id)
        
        if list_review:
            for review in list_review:
                if review.user_id == review_data['user_id']:
                    return {'error': 'You have already reviewed this place'}, 400
                continue
                
        if current_user['id'] != place_data['owner_id']:
            new_review = facade.create_review(review_data)
            return {
                'id': new_review.id ,
                'text': new_review.text,
                'rating': new_review.rating,
                'user_id': new_review.user_id,
                'place_id': new_review.place_id
                }
        
        return {'error':'Cannot review your own place'}
        

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        list_rev = facade.get_all_reviews()
        return marshal(list_rev, review_model), 201

@api.route('/<review_id>')
class ReviewResource(Resource):
    @jwt_required()
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)

        if not review:
            return {'error': 'Review not found'}, 404
        
        return {'id': review.id, 'text': review.text, 'rating': review.rating, 'user_id': review.user_id, 'place_id': review.place_id}

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        scheme = {
            'id': {'type': 'string'},
            'text': {'type': 'string'}, 
            'rating': {'type': 'int'}, 
            'user_id': {'type': 'string'}, 
            'place_id': {'type': 'string'},
            } 
        val = Validator(scheme)
        
        review_data = api.payload
        current_user = get_jwt_identity()
        review = facade.get_place(review_id)
        
        if not review:
            return {'error': 'Review not found'}, 404
        
        is_admin = current_user.get('is_admin')
        
        if is_admin or current_user['id'] == review['user_id']:
            if val.validate(review_data):
                facade.update_review(review_id, review_data)
                return {"message": "Review updated successfully"}, 200
        return {'error': 'Unauthorized action'}, 400

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        current_user = get_jwt_identity()
        is_admin = current_user.get('is_admin')
    
        if is_admin or current_user['id'] == review['user_id']:
            facade.delete_review(review_id)
            return {"message": "Review deleted successfully"}, 200
        return {'error': 'Unauthorized action'}


@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        list_pr = facade.get_reviews_by_place(place_id)
        return list_pr
