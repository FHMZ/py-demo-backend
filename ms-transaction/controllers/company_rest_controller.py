from flask import Blueprint, jsonify, request
from google.protobuf.json_format import MessageToDict
from util import SingletonClass
from validations.company_validation import CompanyValidation
from rabbitmq import RabbitMQ
import uuid
import json
from controllers.company_grpc_controller import CompanyGrpcController
import controllers.proto.company_pb2_grpc
import controllers.proto.company_pb2

CompanyRestControllerBluePrint = Blueprint("controller", __name__)


class CompanyRestController(SingletonClass):
    @CompanyRestControllerBluePrint.route('/api/company/create_company', methods=["POST"])
    def createCompany():
        CompanyValidation().validate_rest_request_body_is_json(request)
        response = CompanyGrpcController().CreateCompany(
            controllers.proto.company_pb2.CreateCompanyRequest(
                legal_entity_registration=request.json.get(
                    'legal_entity_registration'),
                company_id=request.json.get('company_id'),
                company_name=request.json.get('company_name')), {'channel': 'REST'})
        return jsonify(MessageToDict(response)), 200

    @CompanyRestControllerBluePrint.route('/api/company/deactivate_company', methods=["POST"])
    def deactivateCompany():
        CompanyValidation().validate_rest_request_body_is_json(request)
        response = CompanyGrpcController().DeactivateCompany(request, {})
        return jsonify(MessageToDict(response)), 200

    @CompanyRestControllerBluePrint.route('/api/company/reactivate_company', methods=["POST"])
    def reactivateCompany():
        CompanyValidation().validate_rest_request_body_is_json(request)
        respone = CompanyGrpcController().ReactivateCompany(request, {})
        return jsonify(MessageToDict(response)), 200
