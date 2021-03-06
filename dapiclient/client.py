import sys
from MNDiscovery.masternode_discovery import MasternodeDiscovery
from rpc.jsonrpc.jsonrpc_client import JsonRpcClient
from rpc.grpc.grpc_client import GRpcClient

SEED_PORT = 3000
SEED_PORT_GRPC = 3010
GRPC_REQUEST_TIMEOUT = 5
GRPC_MAX_RESULTS = 100

class DAPIClient:
    """docstring for DAPIClient."""

    def __init__(self, options = {}):
        self.mn_discovery = MasternodeDiscovery() #options['seeds'], options['port'])
        self.dapi_port = SEED_PORT #if options.port not in options else options.port
        self.native_grpc_port = SEED_PORT_GRPC #options.nativeGrpcPort || config.grpc.nativePort;
        self.timeout = 2000 #options.timeout || 2000;
        #self.forceJsonRpc = options.forceJsonRpc;
        #preconditionsUtil.checkArgument(jsutil.isUnsignedInteger(self.timeout),
        #  'Expect timeout to be an unsigned integer');
        self.retries = 1 #options.retries ? options.retries : 3;
        #preconditionsUtil.checkArgument(jsutil.isUnsignedInteger(self.retries),
        #  'Expect retries to be an unsigned integer');
        #self.dpp = new DPP();
        #self.make_request = {}
        #self.make_request['call_count'] = 0

    def make_request_to_random_dapi_node(self, method, params = {}, excluded_ips = []):
        #self.make_request['call_count'] = 0;

        return self.make_request_with_retries(method, params, self.retries, excluded_ips);


    def make_request(self, method, params, excluded_ips = []):
        #print(method)
        #self.make_request['call_count'] += 1
        random_masternode = self.mn_discovery.get_random_masternode(excluded_ips)
        #print(random_masternode)
        return JsonRpcClient.request({
          'host': random_masternode.split(':')[0],
          'port': self.dapi_port,
        }, method, params, { 'timeout': self.timeout })


    def make_request_to_node(self, method, params, ip):
        return JsonRpcClient.request({
          'host': ip,
          'port': self.dapi_port,
        }, method, params, { 'timeout': self.timeout })


    def make_request_with_retries(self, method, params, retries_count, excluded_ips):
        try:
            return self.make_request(method, params, excluded_ips)
        except Exception as ex:
            print('Exception:\n{}'.format(ex))
            #if (err.code !== 'ECONNABORTED' && err.code !== 'ECONNREFUSED') {
            #throw err;
          #}
            if (retries_count > 0):
                print('*** Retrying ***')
                excluded_on_next_try = []
                #if (err.address) {
                #  excludedOnNextTry = Array.isArray(excludedIps)
                #    ? excludedIps.slice().push(err.address) : excludedOnNextTry.push(err.address);
                #}
                return self.make_request_with_retries(method, params, retries_count - 1, excluded_on_next_try)

            raise Exception('max retries to connect to DAPI node reached');


    def getBestBlockHash(self):
        return self.make_request_to_random_dapi_node('getBestBlockHash')


    def getBlockHash(self, height):
        return self.make_request_to_random_dapi_node('getBlockHash', {'height': height})


    def getMnListDiff(self, baseBlockHash, blockHash):
        return self.make_request_to_random_dapi_node('getMnListDiff',
            {
                'baseBlockHash': baseBlockHash,
                'blockHash': blockHash
            })


    def getUTXO(self, address, from_result=0, to_result=1000, fromHeight=0, toHeight=sys.maxsize):
        return self.make_request_to_random_dapi_node('getUTXO',
            {
                'address': address,
                'from': from_result,
                'to': to_result,
                'fromHeight': fromHeight,
                'toHeight': toHeight
            })

    # gRPC endpoints

    def make_request_to_random_dapi_grpc_node(self, method, params = {}, options = {}, excluded_ips = []):
        #self.make_request['call_count'] = 0;
        random_masternode = self.mn_discovery.get_random_masternode()
        ip = random_masternode.split(":")[0]
        socket = '{}:{}'.format(ip, self.native_grpc_port)

        options = {
            'timeout': GRPC_REQUEST_TIMEOUT
        }

        return GRpcClient.request(socket, method, params, options)


    def getIdentity(self, id):
        return self.make_request_to_random_dapi_grpc_node(
                'getIdentity',
                {
                    'id': id
                }
            )


    def getDataContract(self, id):
        return self.make_request_to_random_dapi_grpc_node(
                'getDataContract',
                {
                    'id': id
                }
            )

    def getDocuments(self, data_contract_id, document_type, limit=GRPC_MAX_RESULTS, start_at=0):
        # TODO: implement where, order_by, and start_after
        return self.make_request_to_random_dapi_grpc_node(
                'getDocuments',
                {
                    'data_contract_id': data_contract_id,
                    'document_type': document_type,
                    'limit': limit,
                    'start_at': start_at
                }
            )


def main():
    client = DAPIClient()
    return

if __name__ == "__main__":
    main()
