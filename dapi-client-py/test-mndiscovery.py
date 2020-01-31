import json
import time
from MNDiscovery.masternode_discovery import MNDiscovery

def main():
    mnd = MNDiscovery()
    print('Test - Get MN List')
    mnl = mnd.get_mnlist()

    print('Test - Random Node: {}'.format(mnd.get_random_masternode()))

    print('Test - Reset')
    mnd.reset()

    print('Test - Get MN List after reset')
    mnd.get_mnlist()

    print('Test - Get MN List before timeout')
    time.sleep(1)
    mnd.get_mnlist()

    print('Test - Refresh list after timeout')
    time.sleep(60)
    mnd.get_mnlist()

    #print(json.dumps(mnl, indent = 2))

if __name__ == "__main__":
    main()
