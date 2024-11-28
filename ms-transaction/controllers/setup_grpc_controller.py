import controllers.setup_pb2_grpc
from validations.setup_validation import SetupValidation
from rabbitmq import RabbitMQ
import uuid
import json
from google.protobuf.json_format import MessageToDict


class SetupGrpcController(controllers.setup_pb2_grpc.SetupServicer):
    def AddAccount(self, request, context):
        SetupValidation().validate_grpc_add_account(request)
        print(f'REQUEST -> {request.account}')
        trx_id = f"setup.add_account.{uuid.uuid4()}"
        print(f'TRX_ID -> {trx_id}')
        body = json.dumps({
            "trx_id": trx_id,
            "trx_payload": MessageToDict(request),
            "trx_channel": "GRPC"})
        channel = RabbitMQ().get_channel()
        channel.basic_publish(
            exchange='amq.topic',
            routing_key=f"process.{trx_id}",
            body=body)
        return controllers.setup_pb2.AddAccountResponse(
            transaction=controllers.setup_pb2.Transaction(
                trx_id=trx_id
            )
        )
