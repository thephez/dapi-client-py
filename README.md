
# Generating dapi-grpc proto files for Python

```shell
python -m grpc_tools.protoc -Idashevo/dapi-grpc/protos --python_out=. --grpc_python_out=. dashevo/dapi-grpc/protos/core.proto
python -m grpc_tools.protoc -Idashevo/dapi-grpc/protos --python_out=. --grpc_python_out=. dashevo/dapi-grpc/protos/platform.proto
python -m grpc_tools.protoc -Idashevo/dapi-grpc/protos --python_out=. --grpc_python_out=. dashevo/dapi-grpc/protos/transactions_filter_stream.proto

```

To get module imports working properly:
https://stackoverflow.com/a/50193944

From root of repository
```shell
pip install -e
```
