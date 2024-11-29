from flask import Blueprint, jsonify, request
from google.protobuf.json_format import MessageToDict, ParseDict
from util import SingletonClass
from validations.setup_validation import SetupValidation
from rabbitmq import RabbitMQ
import uuid
import json
from controllers.setup_grpc_controller import SetupGrpcController
import controllers.proto.setup_pb2_grpc
import controllers.proto.setup_pb2

SetupRestControllerBluePrint = Blueprint("controller", __name__)
grpc_context = {'channel': 'REST'}


class SetupRestController(SingletonClass):
    @SetupRestControllerBluePrint.route('/api/setup', methods=["POST"])
    def setup():
        SetupValidation().validate_rest_request_body_is_json(request)
        response = SetupGrpcController().Setup(
            ParseDict(request.json,
                      controllers.proto.setup_pb2.SetupRequest()),
            grpc_context,
        )
        return jsonify(MessageToDict(response, preserving_proto_field_name=True)), 200
