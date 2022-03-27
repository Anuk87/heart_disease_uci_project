import mongoengine
from database.models import Tester, Test
from flask_restful import Resource
from flask import Response, request
from validators import validator
from helpers import helpers
from flask_restful import reqparse
from flask_cors import cross_origin


class TestersApi(Resource):
    @cross_origin()
    def get(self):
        """
        :return: all testers in db
        """
        testers = Tester.objects().to_json()
        return Response(testers, mimetype="application/json", status=200)