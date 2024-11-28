# Celero Custom Layer
to run:
```
docker compose up
```
## Proto
```
python -m pip install grpcio-tools
pwd -> ms-transaction/controllers/proto
python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./company.proto
```