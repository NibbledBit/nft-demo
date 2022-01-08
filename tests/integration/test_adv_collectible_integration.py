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
import time


def test_can_create_adv_collectible_integration():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")

    adv_collectible, creation_tx = deploy_advanced_collectible()

    time.sleep(60)
    assert adv_collectible.tokenCounter() == 1
