from brownie import network, config, accounts

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "hardhat",
    "development",
    "ganache-local",
    "mainnet-fork",
]

DECIMALS = 8
STARTING_PRICE = 411200000000


def get_publish_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[1]
    else:
        return accounts.add(config["wallets"]["from_key"])


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])

    #     if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    #     return accounts[2]
    # else:
    #     return accounts.add(config["wallets"]["from_key"])


# def deploy_mocks():
#     print("Deploying Mocks...")
#     if len(MockV3Aggregator) <= 0:
#         MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
#     print("Mocks deployed.")
