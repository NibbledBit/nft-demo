from brownie import network
from scripts import deploy_and_create
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_publish_account,
)
from scripts.deploy_and_create import deploy_simple_collectible
import pytest


def test_token_counter_increments():
    account = get_publish_account()
    simple_collectible = deploy_simple_collectible()
    assert simple_collectible.tokenCounter() == 1


def test_can_create_simple_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    simple_collectible = deploy_simple_collectible()
    assert simple_collectible.ownerOf(0) == get_account()
