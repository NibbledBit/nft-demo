from brownie import SimpleCollectible, AdvancedCollectible, network
from scripts.helpful_scripts import get_account

sample_token_uri = "https://ipfs.io/ipfs/QmVYX1BgugoHzNFsprZHanEYkhWUopUtHmrHsAmTCReABG?filename=nibbles.1.2.json"
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


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
    if len(SimpleCollectible) <= 0:
        print("Deploying SimpleCollectible")
        simple_collectible = SimpleCollectible.deploy({"from": account})
    else:
        simple_collectible = SimpleCollectible[-1]
    print(f"Contract deployed to {simple_collectible}")
    print(f"Token Counter: {simple_collectible.tokenCounter()}")

    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)

    print(
        f"NFT will be viewable at: {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter()-1)}"
    )

    return simple_collectible


def deploy_advanced_collectible():
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
    if len(AdvancedCollectible) <= 0:
        print("Deploying AdvancedCollectible")
        advanced_collectible = AdvancedCollectible.deploy({"from": account})
    else:
        advanced_collectible = AdvancedCollectible[-1]
    print(f"Contract deployed to {advanced_collectible}")
    print(f"Token Counter: {advanced_collectible.tokenCounter()}")

    tx = advanced_collectible.createCollectible({"from": account})
    tx.wait(1)

    print(
        f"NFT will be viewable at: {OPENSEA_URL.format(advanced_collectible.address, advanced_collectible.tokenCounter()-1)}"
    )

    return advanced_collectible


def main():
    deploy_simple_collectible()
    deploy_advanced_collectible()
