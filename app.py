import json
import pickle
import mongoengine
from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Tester, Test
import numpy as np
from validators import validator
from helpers import helpers

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/heart_disease'
}
initialize_db(app)


@app.route('/testers')
def get_testers():
    """
    :return: all testers in db
    """
    testers = Tester.objects().to_json()
    return Response(testers, mimetype="application/json", status=200)


@app.route('/testers/<id>')
def get_tester(id):
    """
    :param id: tester id
    :return: tester data if exists
    """
    try:
        tester = Tester.objects.get(id=id).to_json()
        return Response(tester, mimetype="application/json", status=200)
    except mongoengine.errors.ValidationError:
        res = {
            'error': "Invalid ID",
            'status': 500
        }
        return res, 500


@app.route('/add_tester', methods=['POST'])
def add_tester():
    """
    :return: tester data after saving to db
    """
    try:
        keys = [i for i in request.form.keys()]
        values = [float(j) for j in request.form.values()]
        validated = validator.patient_data_validator(keys, values)

        if validated[0]:
            tester = helpers.list_to_dict(keys, values)
            tester_entry = Tester(**tester).save()
            tester_id = tester_entry.id

            if tester_id:
                val = [float(j) for j in request.form.values()]
                prediction = helpers.predict(val)
                test = {
                    "tester_id": str(tester_id),
                    "result": str(prediction[0]["result"]),
                    "description": str(prediction[0]["message"])
                }
                test_entry = Test(**test).save()
                test_id = test_entry.id

                res = {
                    "message": "Details saved successfully",
                    "tester_id": str(tester_id),
                    "test_id": str(test_id),
                    'status': 200
                }
                return res, 200
        else:
            res = {
                "message": 'Validation error. {error}'.format(error=validated[1]),
                "status": 422
            }
            return res, 422
    except ValueError:
        res = {
            "message": 'Invalid data type for value. Must be a float or int.',
            "status": 422
        }
        return res, 422


@app.route('/testers/<id>', methods=['DELETE'])
def delete_tester(id):
    """
    :param id: tester id
    :return: delete success response
    """
    try:
        Tester.objects.get(id=id).delete()
        res = {
            "message": 'Tester successfully deleted',
            "tester_id": str(id)
        }
        return res, 200
    except mongoengine.errors.ValidationError:
        res = {
            'error': "Invalid ID",
            'status': 500
        }
        return res, 500


@app.route('/tests')
def get_tests():
    """
    :return: all tests in db
    """
    tests = Test.objects().to_json()
    return Response(tests, mimetype="application/json", status=200)


@app.route('/test/<id>')
def get_test(id):
    """
    :param id: test id
    :return: test data if exists
    """
    try:
        test = Test.objects.get(id=id).to_json()
        return Response(test, mimetype="application/json", status=200)
    except mongoengine.errors.ValidationError:
        res = {
            'error': "Invalid ID",
            'status': 500
        }
        return res, 500


@app.route('/tests/<id>', methods=['DELETE'])
def delete_test(id):
    """
    :param id: test id
    :return: delete success response
    """
    try:
        Test.objects.get(id=id).delete()
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


app.run()
