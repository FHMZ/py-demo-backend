import controllers.setup_pb2_grpc


class SetupGrpcController(controllers.setup_pb2_grpc.SetupServicer):
    def AddAccount(self, request, context):
        return controllers.setup_pb2.AddAccountResponse(
            controllers.setup_pb2.Transaction(
                trx_id='setup.add_account.xyz'
            )
        )
