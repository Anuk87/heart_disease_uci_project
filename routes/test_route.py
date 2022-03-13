from controllers.test_controller import TestApi


def initialize_test_routes(api):
    api.add_resource(TestApi, '/api/test/<id>', methods=["GET"])




