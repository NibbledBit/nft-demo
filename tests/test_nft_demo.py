from scripts.helpful_scripts import get_publish_account
from scripts.deploy import deploy_simple_collectible


def test_token_counter_increments():
    account = get_publish_account()
    simple_collectible = deploy_simple_collectible()
    tx = simple_collectible.createCollectible({"from": account})
    tx.wait(1)
    assert simple_collectible.tokenCounter() == 1
