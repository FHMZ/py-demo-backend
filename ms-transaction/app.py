from flask import Flask, jsonify
from rabbitmq import RabbitMQ
from concurrent import futures
import grpc
from multiprocessing import Process
import controllers.proto.setup_pb2
import controllers.proto.setup_pb2_grpc
from controllers.setup_rest_controller import SetupRestControllerBluePrint
from controllers.setup_grpc_controller import SetupGrpcController


def setup_rabbitmq():
    channel = RabbitMQ().get_channel()
    channel.queue_declare(
        queue='setup', durable=True)
    channel.queue_bind(
        queue='setup',
        exchange='amq.topic',
        routing_key='process.setup.setup.*')


def build_api_rest():
    app = Flask(__name__)
    app.register_blueprint(SetupRestControllerBluePrint)
    app.run(host="0.0.0.0", port=5000, debug=True)


def build_api_grpc():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    controllers.proto.setup_pb2_grpc.add_CeleroCustomLayerSetupServicer_to_server(
        SetupGrpcController(),
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
