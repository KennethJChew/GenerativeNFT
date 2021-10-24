from brownie import network,config,accounts


LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache", "mainnet-fork"]
def get_account(index=None,id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    print("Getting real account")
    return accounts.add(config["wallets"]["from_key"])