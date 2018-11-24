# associated medium post: https://medium.com/@ethervolution/ethereum-create-raw-json-rpc-requests-with-python-for-deploying-and-transacting-with-a-smart-7ceafd6790d9
import requests
import json
import web3 # Release 4.0.0-beta.8
import pprint
import time

# create persistent HTTP connection
session = requests.Session()
w3 = web3.Web3()
pp = pprint.PrettyPrinter(indent=2)

requestId = 0 # is automatically incremented at each request

URL = 'http://localhost:8501' # url of my geth node
PATH_GENESIS = '/home/abdullah/devnet/genesis.json'
PATH_SC_TRUFFLE = '/home/abdullah/devnet/workspace/' # smart contract path

# extracting data from the genesis file
genesisFile = json.load(open(PATH_GENESIS))
CHAINID = genesisFile['config']['chainId']
PERIOD  = genesisFile['config']['clique']['period']
GASLIMIT = int(genesisFile['gasLimit'],0)

# compile your smart contract with truffle first
truffleFile = json.load(open(PATH_SC_TRUFFLE + '/build/contracts/AdditionContract.json'))
abi = truffleFile['abi']
bytecode = truffleFile['bytecode']

# Don't share your private key !
myAddress = '0x29a86118C1Ff89d474E9497D8B3FA890D9F7e30C' # address funded in genesis file
myPrivateKey = '0xff8c4769d2e1d6f7bee613c422a1f9243f189bf5f9764c15b19c6439c0f56cd9'
contractAddress = '0x1f9eb9f5c0c94603f6fb1acf19f99ddd76600af7'

''' =========================== SOME FUNCTIONS ============================ '''
# see http://www.jsonrpc.org/specification
# and https://github.com/ethereum/wiki/wiki/JSON-RPC

def createJSONRPCRequestObject(_method, _params, _requestId):
    return {"jsonrpc":"2.0",
            "method":_method,
            "params":_params, # must be an array [value1, value2, ..., valueN]
            "id":_requestId}, _requestId+1
    
def postJSONRPCRequestObject(_HTTPEnpoint, _jsonRPCRequestObject):
    response = session.post(_HTTPEnpoint,
                            json=_jsonRPCRequestObject,
                            headers={'Content-type': 'application/json'})

    return response.json()

''' ================= SEND A TRANSACTION TO SMART CONTRACT  ================'''
### get your nonce
requestObject, requestId = createJSONRPCRequestObject('eth_getTransactionCount', [myAddress, 'latest'], requestId)
responseObject = postJSONRPCRequestObject(URL, requestObject)
myNonce = w3.toInt(hexstr=responseObject['result'])
print('nonce of address {} is {}'.format(myAddress, myNonce))

### prepare the data field of the transaction
# function selector and argument encoding
# https://solidity.readthedocs.io/en/develop/abi-spec.html#function-selector-and-argument-encoding
value1, value2 = 10, 32 # random numbers here
function = 'add(uint256,uint256)' # from smart contract
methodId = w3.sha3(text=function)[0:4].hex()
param1 = (value1).to_bytes(32, byteorder='big').hex()
param2 = (value2).to_bytes(32, byteorder='big').hex()
data = '0x' + methodId + param1 + param2

print (format(data))
print (data)
print (methodId)
print (format(methodId))

