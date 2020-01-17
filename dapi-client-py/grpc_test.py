import grpc

#import route_guide_pb2
#import route_guide_pb2_grpc
#import route_guide_resources
import platform_pb2
import platform_pb2_grpc
#import platform_resources

import cbor

GRPC_REQUEST_TIMEOUT = 5

# Set up connection
channel = grpc.insecure_channel('evonet.thephez.com:3010')
stub = platform_pb2_grpc.PlatformStub(channel)


# Get Identity
identity_id = 'Bb2p582MFR1tQhVQHKrScsAJH6Erqsb6SoroD9dQhJ5e'
# Create Identity request
identity_request = platform_pb2.GetIdentityRequest()
# Set identity parameter of request
identity_request.id = identity_id

identity_response = platform_pb2.GetIdentityResponse()
identity = stub.getIdentity(identity_request, GRPC_REQUEST_TIMEOUT)
print(identity.identity)

#print(dir(identity_response))

# Get Data Contract
dpns_contract_id = '2KfMcMxktKimJxAZUeZwYkFUsEcAZhDKEpQs8GMnpUse'
contract_request = platform_pb2.GetDataContractRequest()
contract_request.id = dpns_contract_id

data_contract = stub.getDataContract(contract_request, GRPC_REQUEST_TIMEOUT)
print(data_contract)


# Get Document
contract_id = dpns_contract_id

document_request = platform_pb2.GetDocumentsRequest()
document_request.data_contract_id = contract_id
document_request.document_type =  'domain'
#document_request.limit =  5
#document_request.where = # Requires cbor

docs = stub.getDocuments(document_request, GRPC_REQUEST_TIMEOUT)
print(docs)
