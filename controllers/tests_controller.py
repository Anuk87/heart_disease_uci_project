import mongoengine
from database.models import Tester, Test
from flask_restful import Resource
from flask import Response, request
from validators import validator
from helpers import helpers
from flask_cors import cross_origin


class TestsApi(Resource):
    @cross_origin()
    def get(self):
        """
        :return: all tests in db
        """
        tests = Test.objects().to_json()
        return Response(tests, mimetype="application/json", status=200)

