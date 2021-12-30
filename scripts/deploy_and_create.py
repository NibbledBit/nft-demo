from brownie import SimpleCollectible, network
from scripts.helpful_scripts import get_account

sample_token_uri = "https://ipfs.io/ipfs/QmRCN6gN4eqx2W3sxmLTojbvZEbRbXKsDQnwaASyM7pZbN?filename=nibbles.1.1.json"
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


def main():
    deploy_simple_collectible()
