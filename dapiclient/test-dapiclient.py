from client import DAPIClient

client = DAPIClient()

current_block_hash = client.getBestBlockHash()
print('Test - getBestBlockHash: {}'.format(current_block_hash))

height = 0
genesis_block_hash = client.getBlockHash(height)
print('Test - getBlockHash (height: {}): {}'.format(height, genesis_block_hash))

mnlist_diff = client.getMnListDiff(genesis_block_hash, current_block_hash)
print('Test - getMnListDiff:\n{}'.format(mnlist_diff))

print('Test - Check for JSON-RPC response from all masternodes')
for mn in mnlist_diff['mnList']:
    ip = mn['service'].split(':')[0]
    try:
        response = client.make_request_to_node('getBestBlockHash', {}, ip)
        print('Successful response from {}: {}'.format(ip, response))
    except Exception as ex:
        print('*** Failure from {} ***'.format(ip))
