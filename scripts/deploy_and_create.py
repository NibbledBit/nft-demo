from brownie import SimpleCollectible, network
from scripts.helpful_scripts import get_account

sample_token_uri = ""


def deploy_simple_collectible():
    # Get Account
    print("Getting account")
    account = get_account()
    print(f"Account {account}")

    # configure dependencies
    print(f"The active network is {network.show_active()}")
    # if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    #     price_feed_address = config["networks"][network.show_active()][
    #         "eth_usd_price_feed"
    #     ]
    # else:
    #     deploy_mocks()
    #     price_feed_address = MockV3Aggregator[-1].address
    # deploying contracts
    print("Deploying SimpleCollectible")
    simple_collectible = SimpleCollectible.deploy({"from": account})

    print(f"Contract deployed to {simple_collectible}")
    print(f"Token Counter: {simple_collectible.tokenCounter()}")
    return simple_collectible


def main():
    deploy_simple_collectible()
