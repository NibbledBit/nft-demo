from brownie import network
from scripts.advanced_collectible.deploy_and_create import deploy_advanced_collectible
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_publish_account,
    get_contract,
)
from scripts.simple_collectible.deploy_and_create import deploy_simple_collectible
import pytest


def test_can_create_adv_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")

    adv_collectible, creation_tx = deploy_advanced_collectible()
    random_number = 777
    requestId = creation_tx.events["requestedCollectible"]["requestId"]
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_number, adv_collectible, {"from": get_account()}
    )
    assert adv_collectible.tokenCounter() == 1
    assert adv_collectible.tokenIdToTrait(0) == random_number % 4
