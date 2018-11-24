import requests
import json
import web3 # Release 4.0.0-beta.8
import pprint
import time

# create persistent HTTP connection
session = requests.Session()
w3 = web3.Web3()

myAddress1 = '0x0337518b10d11ff8c475ab2508ea120e3d7f41e7'
myPrivateKey1 = 'pwdnode1'
myAddress2 = '0x29a86118C1Ff89d474E9497D8B3FA890D9F7e30C'
myPrivateKey2 = '0xff8c4769d2e1d6f7bee613c422a1f9243f189bf5f9764c15b19c6439c0f56cd9'
contractAddress = '0x1f9eb9f5c0c94603f6fb1acf19f99ddd76600af7'

headers = {'Content-type': 'application/json'}
#Finding Nonce
payload= {"jsonrpc":"2.0",
           "method":"eth_getTransactionCount",
           "params": ['0x0337518b10d11ff8c475ab2508ea120e3d7f41e7','latest'], 
           "id":1515}



response = session.post('http://localhost:8501', json=payload, headers=headers)
#print('raw json response: {}'.format(response.json()))
myNonce1 = w3.toInt(hexstr=response.json()['result'])
print('nonce of address {} is {}'.format(myAddress1, myNonce1))


value1, value2 = 10, 32 # random numbers here
function = 'add(uint256,uint256)' # from smart contract
methodId = w3.sha3(text=function)[0:4].hex()
param1 = (value1).to_bytes(32, byteorder='big').hex()
param2 = (value2).to_bytes(32, byteorder='big').hex()
data = '0x' + methodId + param1 + param2


transaction_dict = {
        'to' : contractAddress,
        'value' : 0,
        'chainId' : 1,
        'gas' : 2000000,
        'gasPrice' : 1,
        'nonce' : myNonce1,
        'data' : data
        }


response = session.post('http://localhost:8501', json=payload, headers=headers)    

signedtxn = w3.eth.account.signTransaction(transaction_dict, myPrivateKey2)
params = signedtxn.rawTrasnaction
print (signedtxn)








