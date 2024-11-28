from controllers.setup_rest_controller import setup_rest_controller
from flask import Flask, jsonify
from rabbitmq import RabbitMQ
from concurrent import futures
import logging
import grpc
import controllers.setup_pb2
import controllers.setup_pb2_grpc
from controllers.setup_grpc_controller import SetupGrpcController
from multiprocessing import Process


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
    app.register_blueprint(setup_rest_controller)
    app.run(host="0.0.0.0", port=5000, debug=True)


def build_api_grpc():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    controllers.setup_pb2_grpc.add_SetupServicer_to_server(
        SetupGrpcController(),
        server)
    server.add_insecure_port('[::]:5001')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    # logging.basicConfig()
    setup_rabbitmq()
    grpc_process = Process(target=build_api_grpc)
    rest_process = Process(target=build_api_rest)
    grpc_process.start()
    print("gRPC Server running on port 5001")
    # logger.info("gRPC Server running on port 50051")
    rest_process.start()
    print("REST Server running on port 5000")
    # logger.info("REST Server running on port 5000")
    grpc_process.join()
    rest_process.join()
