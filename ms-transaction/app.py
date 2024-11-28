from flask import Flask, jsonify
from rabbitmq import RabbitMQ
from concurrent import futures
import grpc
from multiprocessing import Process
import controllers.proto.company_pb2
import controllers.proto.company_pb2_grpc
from controllers.company_rest_controller import CompanyRestControllerBluePrint
from controllers.company_grpc_controller import CompanyGrpcController


def setup_rabbitmq():
    channel = RabbitMQ().get_channel()
    channel.queue_declare(
        queue='setup_add_account', durable=True)
    channel.queue_declare(
        queue='logger', durable=True)
    channel.queue_bind(
        queue='setup_add_account',
        exchange='amq.topic',
        routing_key='process.setup.add_account.*')
    channel.queue_bind(
        queue='logger',
        exchange='amq.topic',
        routing_key='*.*.*.*')


def build_api_rest():
    app = Flask(__name__)
    app.register_blueprint(CompanyRestControllerBluePrint)
    app.run(host="0.0.0.0", port=5000, debug=True)


def build_api_grpc():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    controllers.proto.company_pb2_grpc.add_CompanyServicer_to_server(
        CompanyGrpcController(),
        server)
    server.add_insecure_port('[::]:5001')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    setup_rabbitmq()
    grpc_process = Process(target=build_api_grpc)
    rest_process = Process(target=build_api_rest)
    grpc_process.start()
    rest_process.start()
    grpc_process.join()
    rest_process.join()
