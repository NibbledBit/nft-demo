from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import OPENSEA_URL, get_account, get_trait

metadata_dict = {
    "Plain": "https://ipfs.io/ipfs/QmT8SHuB3u3s4MTuCfctJfCjykJzJfvUpnfqjE1KKygEa8?filename=4-Plain.json",
    "Halo": "https://ipfs.io/ipfs/QmYVzTSLNM2J15kb2gL7UF8MRBCXcFh3CafYR824XL9Coz?filename=1-Halo.json",
    "Sunglasses": "https://ipfs.io/ipfs/QmPHyiavQwpapNenTPXt8qLNcG5ESnPbzoDD4RxBfGqdPM?filename=0-Sunglasses.json",
    "Tattoo": "https://ipfs.io/ipfs/QmfEt2Grcm6Nb3jnuzsJ94DbEJ7gr2gGV2LiodnbsaDnjg?filename=3-Tattoo.json",
}


def main():
    print(f"working on {network.show_active()}")
    adv_collect = AdvancedCollectible[-1]
    num_of_collectibles = adv_collect.tokenCounter()
    print(f"You have {num_of_collectibles}")
    for token_id in range(num_of_collectibles):
        trait = get_trait(adv_collect.tokenIdToTrait(token_id))
        # if not adv_collect.tokenURI(token_id).startswith("https://"):
        set_tokenURI(token_id, adv_collect, metadata_dict[trait])


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(f"View NFT at:{OPENSEA_URL.format(nft_contract.address, token_id)}")
