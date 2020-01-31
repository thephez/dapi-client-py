
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



```
python3 -m venv ~/venv/dapiclient
source ~/venv/dapiclient/bin/activate
python setup.py install
pip install requests

python dapiclient/MNDiscovery/masternode_list_provider.py

python dapiclient/test-mndiscovery.py

```
