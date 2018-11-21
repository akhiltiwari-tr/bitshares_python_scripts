from bitshares import BitShares
from bitshares.blockchain import  Blockchain
from pprint import pprint

print("####Begins####")

# creates a connection to a bitshares node.
testnet = BitShares( "ws://0.0.0.0:11011", nobroadcast=True, bundle=True,)
blockchain = Blockchain(testnet)

# wallet creation
# testnet.wallet.create("akhil")
# testnet.wallet.addPrivateKey("5JtyazjyGeFScWH3614tWpGe3xzkxmCrsb4Q2y3WJn883EyW9qT")

# testnet.wallet.unlock("akhil")
for op in blockchain.ops():
    print(op)

# pprint(testnet.wallet.getAccounts())


# bitshares.transfer("<to>", "<amount>", "<asset>", "[<memo>]", account="<from>")