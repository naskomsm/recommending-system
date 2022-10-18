from flask_restful import Resource, reqparse

class HealthResource(Resource):
    def get(self):
        return {"status": "ok"}, 200
