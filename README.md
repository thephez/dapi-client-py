
# Generating dapi-grpc proto files for Python

```shell
python -m grpc_tools.protoc -Idashevo/dapi-grpc/protos --python_out=. --grpc_python_out=. dashevo/dapi-grpc/protos/core.proto
python -m grpc_tools.protoc -Idashevo/dapi-grpc/protos --python_out=. --grpc_python_out=. dashevo/dapi-grpc/protos/platform.proto
python -m grpc_tools.protoc -Idashevo/dapi-grpc/protos --python_out=. --grpc_python_out=. dashevo/dapi-grpc/protos/transactions_filter_stream.proto

```
