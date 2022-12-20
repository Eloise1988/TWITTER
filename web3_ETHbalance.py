from web3 import Web3

#Insert Infura API Key in URL
url='https://mainnet.infura.io/v3/YOUR-API-KEY'
web3 = Web3(Web3.HTTPProvider(url))

balance = web3.eth.getBalance(web3.toChecksumAddress("0x1234........r9"))
balance_in_ether = balance / 10**18
print(balance_in_ether)
