from client import DAPIClient
import cbor2

client = DAPIClient()


def jsonrpc_tests():
    current_block_hash = client.getBestBlockHash()
    print('Test - getBestBlockHash: {}\n'.format(current_block_hash))

    height = 0
    genesis_block_hash = client.getBlockHash(height)
    print('Test - getBlockHash (height: {}): {}\n'.format(height, genesis_block_hash))

    mnlist_diff = client.getMnListDiff(genesis_block_hash, current_block_hash)
    print('Test - getMnListDiff:\n{}\n'.format(mnlist_diff))

    utxo = client.getUTXO('yPprxZrUL8UN73qLDS2xCg6yBFGieUWz7Q')#, 2)
    print('Test - getUTXO:\n{}\n'.format(utxo))

    return mnlist_diff

# gRPC
def grpc_tests():
    id = client.getIdentity('Bb2p582MFR1tQhVQHKrScsAJH6Erqsb6SoroD9dQhJ5e')
    print('Test - getIdentity:\n{}\n'.format(id))

    contract = client.getDataContract('2KfMcMxktKimJxAZUeZwYkFUsEcAZhDKEpQs8GMnpUse')
    print('Test - getDataContract:\n{}\n'.format(contract))

    docs = client.getDocuments(
        '2KfMcMxktKimJxAZUeZwYkFUsEcAZhDKEpQs8GMnpUse',
        'domain',
        limit=5,
        start_at=2
    )
    print('Test - getDocuments: {} documents retrieved (max of 100)'.format(len(docs)))
    for doc in docs:
        print('Document:\n\t{}\n'.format(cbor2.loads(doc)))


#raise Exception('exit execution early')

def jsonrpc_comm_test(mnlist_diff):
    print('Test - Check for JSON-RPC response from all masternodes')
    for mn in mnlist_diff['mnList']:
        ip = mn['service'].split(':')[0]
        try:
            response = client.make_request_to_node('getBestBlockHash', {}, ip)
            print('Successful response from {}: {}'.format(ip, response))
        except Exception as ex:
            print('*** Failure from {} ***'.format(ip))


def main():
    mnlist_diff = jsonrpc_tests()

    #jsonrpc_comm_test(mnlist_diff)

    grpc_tests()


if __name__ == "__main__":
    main()
