
# Quickstart


```
git clone https://github.com/thephez/dapi-client-py.git
cd dapi-client-py
python3 -m venv dapiclient-venv
source dapiclient-venv/bin/activate
pip install -r requirements.txt
python setup.py install

# Check masternode list
python dapiclient/test-mndiscovery.py

# Check DAPI client functionality
python dapiclient/test-dapiclient.py
```

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


