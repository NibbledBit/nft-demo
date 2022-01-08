from brownie import AdvancedCollectible, network, config
from scripts.helpful_scripts import (
    get_account,
    OPENSEA_URL,
    get_contract,
    fund_with_link,
)

sample_token_uri = "https://ipfs.io/ipfs/QmVYX1BgugoHzNFsprZHanEYkhWUopUtHmrHsAmTCReABG?filename=nibbles.1.2.json"


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

    print("Deploying AdvancedCollectible")
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {advanced_collectible}")
    print(f"Token Counter: {advanced_collectible.tokenCounter()}")

    fund_with_link(advanced_collectible.address)

    tx = advanced_collectible.createCollectible({"from": account})
    tx.wait(1)

    return advanced_collectible, tx


def main():
    deploy_advanced_collectible()
