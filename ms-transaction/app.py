from controllers.setup_controller import setup_controller
from flask import Flask, jsonify
import pika

app = Flask(__name__)
app.register_blueprint(setup_controller)

if __name__ == "__main__":
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            credentials=pika.credentials.PlainCredentials('admin', 'celero123')
        )
    )
    channel = connection.channel()
    app.run(host="0.0.0.0", port=5000)
