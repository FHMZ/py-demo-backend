import controllers.proto.setup_pb2_grpc
import controllers.proto.setup_pb2
from validations.setup_validation import SetupValidation
from rabbitmq import RabbitMQ
import uuid
import json
from google.protobuf.json_format import MessageToDict


class SetupGrpcController(controllers.proto.setup_pb2_grpc.CeleroCustomLayerSetupServicer):
    def Setup(self, request, context):
        SetupValidation().validate_grpc_setup(request)
        trx_id = f"setup.setup.{uuid.uuid4()}"
        channel = context.get('channel') if isinstance(
            context, dict) and context and 'channel' in context else "GRPC"
        body = json.dumps({
            "trx_id": trx_id,
            "trx_payload": MessageToDict(request, preserving_proto_field_name=True),
            "trx_channel": channel})
        channel = RabbitMQ().get_channel()
        channel.basic_publish(
            exchange='amq.topic',
            routing_key=f"process.{trx_id}",
            body=body)
        return controllers.proto.setup_pb2.SetupResponse(
            transaction_id=trx_id
        )
