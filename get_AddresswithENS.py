from web3 import Web3

#Insert infura authentification key
url='https://mainnet.infura.io/v3/e567xxxxxxxxxxxxxxxxxxxxxxx'
web3 = Web3(Web3.HTTPProvider(url))

eth_address = web3.ens.address(name='ethereum.eth')
print(eth_address)
