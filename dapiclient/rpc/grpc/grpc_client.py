import grpc
import cbor2

# Generated from dapi-grpc
import rpc.grpc.core_pb2 as core_pb2
import rpc.grpc.core_pb2_grpc as core_pb2_grpc
import rpc.grpc.platform_pb2 as platform_pb2
import rpc.grpc.platform_pb2_grpc as platform_pb2_grpc


class GRpcClient:

    def __init__(self):
        pass

    def request(socket, method, params = {}, options = {'timeout': 5}):
        channel = grpc.insecure_channel(socket)
        #print(socket)

        stub = platform_pb2_grpc.PlatformStub(channel)
        stubCore = core_pb2_grpc.CoreStub(channel)

        if method == 'getIdentity':
            return GRpcClient.getIdentity(stub, params, options)

        elif method == 'getDataContract':
            return GRpcClient.getDataContract(stub, params, options)

        elif method == 'getDocuments':
            return GRpcClient.getDocuments(stub, params, options)

        elif method == 'getBlock':
            return GRpcClient.getBlock(stubCore, params, options)

        elif method == 'getStatus':
            return GRpcClient.getStatus(stubCore, params, options)
        elif method == 'getTransaction':
            return GRpcClient.getTransaction(stubCore, params, options)
        else:
            raise ValueError('Unknown gRPC endpoint: {}'.format(method))


    def getIdentity(stub, params, options):
        # Create Identity request
        identity_request = platform_pb2.GetIdentityRequest()
        # Set identity parameter of request
        identity_request.id = params['id']

        response = stub.getIdentity(identity_request, options['timeout'])
        return cbor2.loads(response.identity)


    def getDataContract(stub, params, options):
        contract_request = platform_pb2.GetDataContractRequest()
        contract_request.id = params['id']

        response = stub.getDataContract(contract_request, options['timeout'])
        #print('Data Contract: {}\n'.format(cbor2.loads(response.data_contract)))

        return cbor2.loads(response.data_contract)


    def getDocuments(stub, params, options):
        #print(params)

        document_request = platform_pb2.GetDocumentsRequest()
        document_request.data_contract_id = params['data_contract_id']
        document_request.document_type =  params['document_type']
        document_request.limit =  params['limit']
        document_request.start_at =  params['start_at']

        response = stub.getDocuments(document_request, options['timeout'])

        #for d in response.documents:
        #    print('Document cbor: {}\n'.format(cbor2.loads(d)))

        return response.documents

    def getBlock(stubCore, params, options):
        block_request = core_pb2.GetBlockRequest()
        block_request.hash = params['hash']
        block_request.height = params['height']

        response = stubCore.getBlock(block_request, options['timeout'])
        return cbor2.loads(response.block)

    def getStatus(stubCore, params, options):
        status_request = core_pb2.GetStatusRequest()

        response = stubCore.getStatus(status_request, options['timeout'])

        return response

    def getTransaction(stubCore, params, options):
        transaction_request = core_pb2.GetTransactionRequest()
        transaction_request.id = params['id']

        response = stubCore.getTransaction(transaction_request, options['timeout'])

        return cbor2.loads(response.transaction)
