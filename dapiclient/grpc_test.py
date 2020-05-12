import grpc

import rpc.grpc.core_pb2 as core_pb2
import rpc.grpc.core_pb2_grpc as core_pb2_grpc
import rpc.grpc.platform_pb2 as platform_pb2
import rpc.grpc.platform_pb2_grpc as platform_pb2_grpc
import rpc.grpc.transactions_filter_stream_pb2 as transactions_filter_stream_pb2
import rpc.grpc.transactions_filter_stream_pb2_grpc as transactions_filter_stream_pb2_grpc
#import platform_resources

import cbor2
import base64

GRPC_REQUEST_TIMEOUT = 5

# Set up connection
channel = grpc.insecure_channel('evonet.thephez.com:3010')
stub = platform_pb2_grpc.PlatformStub(channel)
stubCore = core_pb2_grpc.CoreStub(channel)
stubTransactions = transactions_filter_stream_pb2_grpc.TransactionsFilterStreamStub(channel)

def get_identity(id):
    # Get Identity
    #identity_id = 'Bb2p582MFR1tQhVQHKrScsAJH6Erqsb6SoroD9dQhJ5e'
    # Create Identity request
    get_identity_request = platform_pb2.GetIdentityRequest()
    # Set identity parameter of request
    get_identity_request.id = id

    #get_identity_response = platform_pb2.GetIdentityResponse()
    get_identity_response = stub.getIdentity(get_identity_request, GRPC_REQUEST_TIMEOUT)
    #print(get_identity_response)
    print('Identity Response: {}\n'.format(cbor2.loads(get_identity_response.identity)))

    #print(dir(identity_response))

def get_data_contract(contract_id):
    # Get Data Contract
    #dpns_contract_id = '2KfMcMxktKimJxAZUeZwYkFUsEcAZhDKEpQs8GMnpUse'
    contract_request = platform_pb2.GetDataContractRequest()
    contract_request.id = contract_id

    data_contract = stub.getDataContract(contract_request, GRPC_REQUEST_TIMEOUT)
    print(data_contract)
    print('Data Contract: {}\n'.format(cbor2.loads(data_contract.data_contract)))

def get_documents(contract_id, type, options):
    # Get Document
    #contract_id = dpns_contract_id

    document_request = platform_pb2.GetDocumentsRequest()
    document_request.data_contract_id = contract_id
    document_request.document_type =  type
    document_request.limit =  2
    #document_request.where = # Requires cbor (found in dapi-client)

    docs = stub.getDocuments(document_request, GRPC_REQUEST_TIMEOUT)
    #print(docs)
    for d in docs.documents:
        print('Document cbor: {}\n'.format(cbor2.loads(d)))

def get_block(hash=0,height=0):
    # Get Block
    block_request = core_pb2.GetBlockRequest()
    block_request.hash = hash
    block_request.height = height

    block_response = stubCore.getBlock(block_request, GRPC_REQUEST_TIMEOUT)
    print('Block: {}\n'.format(block_response.block))

def get_status():
    status_request = core_pb2.GetStatusRequest()

    status_response = stubCore.getStatus(status_request, GRPC_REQUEST_TIMEOUT)
    print('Status: {}\n'.format(status_response))

def get_transaction(id):
    transaction_request = core_pb2.GetTransactionRequest()
    transaction_request.id = id

    transaction_response = stubCore.getTransaction(transaction_request, GRPC_REQUEST_TIMEOUT)
    print('Transaction: {}\n'.format(transaction_response.transaction))

def send_transaction(transaction, allow_high_fees=0, bypass_limits=0):
    transaction_request = core_pb2.SendTransactionRequest()
    transaction_request.transaction = transaction
    transaction_request.allow_high_fees = allow_high_fees
    transaction_request.bypass_limits = bypass_limits

    transaction_response = stubCore.sendTransaction(transaction_request, GRPC_REQUEST_TIMEOUT)
    print('Transaction: {}\n'.format(transaction_response))

def subscribeToTransactionsWithProofs(bloom_filter, from_block_hash=b'', from_block_height=0, count=0, send_transaction_hashes=0):
    subscribe_request = transactions_filter_stream_pb2.TransactionsWithProofsRequest()
    subscribe_request.from_block_hash = from_block_hash
    subscribe_request.from_block_height = from_block_height
    subscribe_request.count = count
    subscribe_request.send_transaction_hashes = send_transaction_hashes
    setattr(subscribe_request.bloom_filter,'n_hash_funcs',bloom_filter['n_hash_funcs'])
    setattr(subscribe_request.bloom_filter,'v_data',bloom_filter['v_data'])
    setattr(subscribe_request.bloom_filter,'n_tweak',bloom_filter['n_tweak'])
    setattr(subscribe_request.bloom_filter,'n_flags',bloom_filter['n_flags'])

    response = stubTransactions.subscribeToTransactionsWithProofs(subscribe_request, GRPC_REQUEST_TIMEOUT)
    
    return response

def main():
    identity_id = 'JCaTiRxm4dRN1GJqoNkpowmvisC7BbgPW48pJ6roLSgw'
    dpns_contract_id = '5wpZAEWndYcTeuwZpkmSa8s49cHXU5q2DhdibesxFSu8'
    transaction_id = '29b68163a22d89c14e24f1281cb4608b8dc7be05bc2604e2cecf8a85b1dede0d'

    bloom_filter = {
        "n_hash_funcs": 11,
        "v_data": b'',
        "n_tweak": 0,
        "n_flags": 0
    }


    subscribeToTransactionsWithProofs(bloom_filter,from_block_height=1,count=1,send_transaction_hashes=0)
    get_identity(identity_id)
    get_data_contract(dpns_contract_id)
    get_documents(dpns_contract_id, 'note', 'limit = 2')
    get_block('000000079cac3c9e8f40d200589d3935df984fcb89bbbe46f24653b7ccfb5e9c',1)
    get_status()
    get_transaction(transaction_id)
    send_transaction(b'020000000123c52118bfc5da0222a569d379ce3e3a9ca18976175785fd45b3f8990341768b000000006b483045022100a3952306ccb38e1eb22d9956ab40744b79e3072621e634e19225ad8a15603e3102201a3724cb9a8216e78139793c953245b0890c207e13af86bb02735f50a5bccad9012103439cfc2b5fab7fe05c0fbf8fa9217707a5bf5badb7c7e6db05bd0fb1231c5c8bfeffffff0200e1f505000000001976a91468b39aad690ffb710b4ba522d742670b763b501988ac1ec34f95010000001976a91445ada709129f7b6381559c8a16f1ec83c0b3ca8c88acb4240000')

if __name__ == "__main__":
    main()
