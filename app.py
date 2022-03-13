import json
import pickle
import mongoengine
from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Tester, Test
import numpy as np
from validators import validator
from helpers import helpers
from flask_restful import Api
from routes.tester_route import initialize_tester_routes
from routes.test_route import initialize_test_routes
from routes.tests_route import initialize_tests_routes
from routes.testers_route import initialize_testers_routes
from routes.delete_test_route import initialize_delete_test_routes

app = Flask(__name__)
api = Api(app)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/heart_disease'
}
initialize_db(app)
initialize_tester_routes(api)
initialize_testers_routes(api)
initialize_test_routes(api)
initialize_tests_routes(api)
initialize_delete_test_routes(api)

if __name__ == '__main__':
    app.run()
