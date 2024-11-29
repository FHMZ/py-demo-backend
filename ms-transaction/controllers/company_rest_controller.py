from flask import Blueprint, jsonify, request
from google.protobuf.json_format import MessageToDict, ParseDict
from util import SingletonClass
from validations.company_validation import CompanyValidation
from rabbitmq import RabbitMQ
import uuid
import json
from controllers.company_grpc_controller import CompanyGrpcController
import controllers.proto.company_pb2_grpc
import controllers.proto.company_pb2

CompanyRestControllerBluePrint = Blueprint("controller", __name__)
grpc_context = {'channel': 'REST'}


class CompanyRestController(SingletonClass):
    @CompanyRestControllerBluePrint.route('/api/company/create_company', methods=["POST"])
    def createCompany():
        CompanyValidation().validate_rest_request_body_is_json(request)
        response = CompanyGrpcController().CreateCompany(
            ParseDict(request.json,
                      controllers.proto.company_pb2.CreateCompanyRequest()),
            grpc_context,
        )
        return jsonify(MessageToDict(response, preserving_proto_field_name=True)), 200

    @ CompanyRestControllerBluePrint.route('/api/company/deactivate_company', methods=["POST"])
    def deactivateCompany():
        CompanyValidation().validate_rest_request_body_is_json(request)
        response = CompanyGrpcController().DeactivateCompany(
            ParseDict(
                request.json, controllers.proto.company_pb2.DeactivateCompanyRequest()),
            grpc_context,
        )
        return jsonify(MessageToDict(response, preserving_proto_field_name=True)), 200

    @ CompanyRestControllerBluePrint.route('/api/company/reactivate_company', methods=["POST"])
    def reactivateCompany():
        CompanyValidation().validate_rest_request_body_is_json(request)
        response = CompanyGrpcController().ReactivateCompany(
            ParseDict(
                request.json, controllers.proto.company_pb2.ReactivateCompanyRequest()),
            grpc_context,
        )
        return jsonify(MessageToDict(response, preserving_proto_field_name=True)), 200
