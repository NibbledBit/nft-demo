from brownie import network
from scripts.SimpleCollectible import deploy_and_create
from scripts.AdvancedCollectible import deploy_and_create
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_publish_account,
)
from scripts.SimpleCollectible.deploy_and_create import deploy_simple_collectible
import pytest


def test_token_counter_adv_increments():
    account = get_publish_account()
    adv_collectible = deploy_and_create()
    assert adv_collectible.tokenCounter() == 1


def test_can_create_adv_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    adv_collectible = deploy_and_create()
    assert adv_collectible.ownerOf(0) == get_account()
