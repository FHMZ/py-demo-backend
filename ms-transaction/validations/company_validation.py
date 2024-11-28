from util import SingletonClass


class CompanyValidation(SingletonClass):
    def validate_rest_request_body_is_json(self, request):
        if request.is_json == False:
            raise Exception('HTTP Request Body must be JSON')
        pass

    def validate_grpc_create_company(self, request):
        pass

    def validate_grpc_deactivate_company(self, request):
        pass

    def validate_grpc_reactivate_company(self, request):
        pass
