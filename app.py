# Flask
from flask import Flask
from flask_restful import Api

from resources.health import HealthResource
from resources.recommender import RecommenderResource

app = Flask(__name__)
app.secret_key = 'secret'

api = Api(app)

api.add_resource(HealthResource, '/health')
api.add_resource(RecommenderResource, '/recommend')

if __name__ == '__main__':
    app.config['BUNDLE_ERRORS'] = True
    app.run(port=5000, debug=True)
