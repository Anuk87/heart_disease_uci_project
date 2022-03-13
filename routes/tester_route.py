from controllers.tester_controller import TesterApi
from controllers.test_controller import TestApi


def initialize_tester_routes(api):
    api.add_resource(TesterApi, '/api/testers/<string:id>', endpoint='get', methods=["GET"])
    api.add_resource(TesterApi, '/api/add_tester', endpoint='post', methods=["POST"])
    api.add_resource(TesterApi, '/api/delete_tester/<id>', endpoint='delete', methods=["DELETE"])
