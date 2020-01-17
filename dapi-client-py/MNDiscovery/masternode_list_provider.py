import requests
import json
import random

RPC_VERSION = '2.0'
url = 'http://evonet.thephez.com:3000/'

'''
 * This class holds the valid deterministic masternode list
 * @type {SimplifiedMNListEntry[]}
 * @property {string} proRegTxHash
 * @property {string} confirmedHash
 * @property {string} service - ip and port
 * @property {string} pubKeyOperator - operator public key
 * @property {string} keyIDVoting - public key hash, 20 bytes
 * @property {boolean} isValid
'''
class SimplifiedMNListEntry:
    def __init__(self):
        #self.mn_service = set()
        self.mn_entry = []

    def add_entry(self, entry):
        self.mn_entry.append(entry)

    #def add_service(self, service):
    #    self.mn_service.add(service)

    def get_random_masternode(self):
        return random.sample(self.mn_entry, 1)[0]['service']

def dapi_rpc(method, params = {}, id = 1):
    payload = {
        'jsonrpc': RPC_VERSION,
        'params': params,
        'method': method,
        'id': id
        }
    #print(payload)
    headers = {'content-type': 'application/json'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    parsed = json.loads(response.text)
    #print('{} response:\n{}\n\n'.format(method, json.dumps(parsed, indent=4, sort_keys=True)))
    return parsed['result']


def main():
    params = { 'height': 0 }
    genesis_block_hash = dapi_rpc('getBlockHash', params)

    current_block_hash = dapi_rpc('getBestBlockHash')

    method = 'getBlockHeaders'
    params = { 'offset': 1, 'limit': 1 }
    dapi_rpc(method, params)

    method = 'getMnListDiff'
    params = {
        'baseBlockHash': genesis_block_hash,
        'blockHash': current_block_hash
    }
    masternode_list_diff = dapi_rpc(method, params)

    masternode_list = masternode_list_diff['mnList']

    mnl = SimplifiedMNListEntry()
    print('Masternode list contain {} masternodes'.format(len(masternode_list)))

    for mn in masternode_list:
        mnl.add_entry(mn)

    random_mn = mnl.get_random_masternode()
    print('Random MN: {}'.format(random_mn))

if __name__ == "__main__":
    main()
