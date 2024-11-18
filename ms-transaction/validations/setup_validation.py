from util import SingletonClass


class SetupValidation(SingletonClass):
    def validate_add_account(self, request):
        if request.is_json == False:
            raise Exception('HTTP Request Body must be JSON')
        pass
