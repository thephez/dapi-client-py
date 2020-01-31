import grpc

#import route_guide_pb2
#import route_guide_pb2_grpc
#import route_guide_resources
import rpc.grpc.platform_pb2 as platform_pb2
import rpc.grpc.platform_pb2_grpc as platform_pb2_grpc
#import platform_resources

import cbor2

GRPC_REQUEST_TIMEOUT = 5

# Set up connection
channel = grpc.insecure_channel('evonet.thephez.com:3010')
stub = platform_pb2_grpc.PlatformStub(channel)


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
    #print(data_contract)
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

def main():
    identity_id = 'Bb2p582MFR1tQhVQHKrScsAJH6Erqsb6SoroD9dQhJ5e'
    dpns_contract_id = '2KfMcMxktKimJxAZUeZwYkFUsEcAZhDKEpQs8GMnpUse'

    get_identity(identity_id)
    get_data_contract(dpns_contract_id)
    get_documents(dpns_contract_id, 'domain', 'limit = 2')

if __name__ == "__main__":
    main()
