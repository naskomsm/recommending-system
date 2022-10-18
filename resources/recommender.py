from flask_restful import Resource, reqparse


class RecommenderResource(Resource):

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument(
            'whisky_name',
            type=int,
            required=True,
            help=REQURED_FIELD
        )

        data = parser.parse_args()
        print(data)
        return "working", 200
