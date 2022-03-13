import mongoengine
from database.models import Tester, Test
from flask_restful import Resource
from flask import Response, request
from validators import validator
from helpers import helpers


class TestApi(Resource):
    def get(self, id):
        """
        :param id: test id
        :return: test data if exists
        """
        try:
            test = Test.objects().get(id=id).to_json()
            return Response(test, mimetype="application/json", status=200)
        except mongoengine.errors.ValidationError:
            res = {
                'error': "Invalid ID",
                'status': 500
            }
            return res, 500

    def delete(self, id):
        """
        :param id: test id
        :return: delete success response
        """
        try:
            Test.objects().get(id=id).delete()
            res = {
                "message": 'Test successfully deleted',
                "test_id": str(id)
            }
            return res, 200
        except mongoengine.errors.ValidationError:
            res = {
                'error': "Invalid ID",
                'status': 500
            }
            return res, 500
