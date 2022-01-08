from brownie import AdvancedCollectible
from web3 import Web3
from scripts.helpful_scripts import fund_with_link, get_account


def main():
    account = get_account()
    adv_collectible = AdvancedCollectible[-1]
    fund_with_link(adv_collectible.address, amount=Web3.toWei(0.1, "ether"))
    create_trx = adv_collectible.createCollectible({"from": account})
    create_trx.wait(1)
    create_trx = adv_collectible.createCollectible({"from": account})
    create_trx.wait(1)
    create_trx = adv_collectible.createCollectible({"from": account})
    create_trx.wait(1)
    create_trx = adv_collectible.createCollectible({"from": account})
    create_trx.wait(1)
    create_trx = adv_collectible.createCollectible({"from": account})
    create_trx.wait(1)
    print("Created")
