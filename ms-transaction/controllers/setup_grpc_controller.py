import controllers.setup_pb2_grpc
import uuid


class SetupGrpcController(controllers.setup_pb2_grpc.SetupServicer):
    def AddAccount(self, request, context):
        trx_id = f"setup.add_account.{uuid.uuid4()}"
        print(f'TRX_ID -> {trx_id}')
        return controllers.setup_pb2.AddAccountResponse(
            transaction=controllers.setup_pb2.Transaction(
                trx_id=trx_id
            )
        )
