from flask_restful import Resource, reqparse
from services import recommender

class RecommenderResource(Resource):

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument(
            'whisky_name',
            type=str,
            required=True,
            help='This field is required!'
        )

        data = parser.parse_args()
        whisky_name = data['whisky_name']
        
        result = list(recommender.run_recommender(whisky_name))
        return result, 200
