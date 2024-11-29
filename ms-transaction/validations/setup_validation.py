from util import SingletonClass


class SetupValidation(SingletonClass):
    def validate_rest_request_body_is_json(self, request):
        if request.is_json == False:
            raise Exception('HTTP Request Body must be JSON')
        pass

    def validate_grpc_setup(self, request):
        pass