import controllers.proto.company_pb2_grpc
import controllers.proto.company_pb2
from validations.company_validation import CompanyValidation
from rabbitmq import RabbitMQ
import uuid
import json
from google.protobuf.json_format import MessageToDict


class CompanyGrpcController(controllers.proto.company_pb2_grpc.CompanyServicer):
    def CreateCompany(self, request, context):
        CompanyValidation().validate_grpc_create_company(request)
        trx_id = f"setup.add_account.{uuid.uuid4()}"
        body = json.dumps({
            "trx_id": trx_id,
            "trx_payload": MessageToDict(request),
            "trx_channel": "GRPC"})
        channel = RabbitMQ().get_channel()
        channel.basic_publish(
            exchange='amq.topic',
            routing_key=f"process.{trx_id}",
            body=body)
        return controllers.proto.company_pb2.CompanyCommandResponse(
            command_id=trx_id
        )

    def DeactivateCompany(self, request, context):
        CompanyValidation().validate_grpc_deactivate_company(request)
        trx_id = f"company.deactivate_company.{uuid.uuid4()}"
        pass

    def ReactivateCompany(self, request, context):
        CompanyValidation().validate_grpc_reactivate_company(request)
        trx_id = f"company.reactivate_company.{uuid.uuid4()}"
        pass
