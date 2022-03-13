from controllers.tests_controller import TestsApi


def initialize_tests_routes(api):
    api.add_resource(TestsApi, '/api/tests', methods=["GET"])
