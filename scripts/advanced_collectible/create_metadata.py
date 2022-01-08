from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_trait
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import json
import os


def main():
    adv_collectible = AdvancedCollectible[-1]
    number_of_advance_collectibles = adv_collectible.tokenCounter()
    print(f"Amount of collectibles {number_of_advance_collectibles}")
    for token_id in range(number_of_advance_collectibles):
        trait = get_trait(adv_collectible.tokenIdToTrait(token_id))
        metadata_filename = (
            f"./metadata/{network.show_active()}/{token_id}-{trait}.json"
        )
        print(metadata_filename)

        collectible_metadata = metadata_template
        if Path(metadata_filename).exists():
            print(f"metadata {metadata_filename} already exists!")
        else:
            print(f"creating metadata {metadata_filename}")
            collectible_metadata["name"] = trait
            collectible_metadata["description"] = f"This is a {trait} NFT!"
            print(collectible_metadata)
            image_path = "./assets/" + trait.lower().replace("_", "-") + ".jpg"
            if os.getenv("UPLOAD_IPFS"):
                image_uri = upload_to_ipfs(image_path)
            collectible_metadata["image"] = image_uri
            with open(metadata_filename, "w") as file:
                json.dump(collectible_metadata, file)
            if os.getenv("UPLOAD_IPFS"):
                upload_to_ipfs(metadata_filename)


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_bin = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_bin})
        ipfs_hash = response.json()["Hash"]
        # "./assets/trait.jpg"
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
