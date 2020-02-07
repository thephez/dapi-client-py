import grpc
import cbor2

# Generated from dapi-grpc
import rpc.grpc.platform_pb2 as platform_pb2
import rpc.grpc.platform_pb2_grpc as platform_pb2_grpc


class GRpcClient:

    def __init__(self):
        pass

    def request(socket, method, params = {}, options = {'timeout': 5}):
        channel = grpc.insecure_channel(socket)
        #print(socket)

        if method == 'getIdentity':
            return GRpcClient.getIdentity(channel, params, options)

        elif method == 'getDataContract':
            return GRpcClient.getDataContract(channel, params, options)

        elif method == 'getDocuments':
            return GRpcClient.getDocuments(channel, params, options)

        else:
            raise ValueError('Unknown gRPC endpoint: {}'.format(method))


    def getIdentity(channel, params, options):
        stub = platform_pb2_grpc.PlatformStub(channel)

        # Create Identity request
        identity_request = platform_pb2.GetIdentityRequest()
        # Set identity parameter of request
        identity_request.id = params['id']

        response = stub.getIdentity(identity_request, options['timeout'])
        return cbor2.loads(response.identity)


    def getDataContract(channel, params, options):
        stub = platform_pb2_grpc.PlatformStub(channel)

        contract_request = platform_pb2.GetDataContractRequest()
        contract_request.id = params['id']

        response = stub.getDataContract(contract_request, options['timeout'])
        #print('Data Contract: {}\n'.format(cbor2.loads(response.data_contract)))

        return cbor2.loads(response.data_contract)


    def getDocuments(channel, params, options):
        stub = platform_pb2_grpc.PlatformStub(channel)
        #print(params)

        document_request = platform_pb2.GetDocumentsRequest()
        document_request.data_contract_id = params['data_contract_id']
        document_request.document_type =  params['document_type']
        document_request.limit =  params['limit']
        document_request.start_at =  params['start_at']

        response = stub.getDocuments(document_request, options['timeout'])
        #print('Data Contract: {}\n'.format(cbor2.loads(response.data_contract)))

        #for d in response.documents:
        #    print('Document cbor: {}\n'.format(cbor2.loads(d)))

        return response.documents
