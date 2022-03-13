from controllers.testers_controller import TestersApi


def initialize_testers_routes(api):
    api.add_resource(TestersApi, '/api/testers', methods=["GET"])
