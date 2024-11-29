from util import SingletonClass


class SetupComponent(SingletonClass):
    def create_bank_from_amqpb(self, message):
        payload = message.get('trx_payload')
        return {
            'bank_branch': payload.get('bank_branch'),
            'bank_account_number': payload.get('bank_account_number'),
        }

    def create_company_from_amqpb(self, message):
        payload = message.get('trx_payload')
        return {
            'account_digit': payload.get('account_digit'),
            'account_type': payload.get('account_type'),
            'account_office': payload.get('account_office'),
            'account_currency': payload.get('account_currency'),
            'account_manager_email': payload.get('account_manager_email'),
            'account_external_id': payload.get('account_external_id'),
        }

    def create_account_from_amqpb(self, message):
        payload = message.get('trx_payload')
        return {
            'company_identity': payload.get('company_identity'),
            'company_name': payload.get('company_name'),
        }

    def create_user_from_amqpb(self, message):
        payload = message.get('trx_payload')
        return {
            'user_first_name': payload.get('user_first_name'),
            'user_last_name': payload.get('user_last_name'),
            'user_email': payload.get('user_email'),
            'user_phone_area_code': payload.get('user_phone_area_code'),
            'user_phone_number': payload.get('user_phone_number'),
            'user_identity': payload.get('user_identity'),
            'user_birth_date': payload.get('user_birth_date'),
        }
