from controllers.delete_test_controller import DeleteTestApi


def initialize_delete_test_routes(api):
    api.add_resource(DeleteTestApi, '/api/tests/<id>', methods=["DELETE"])



