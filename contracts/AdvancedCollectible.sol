// SPDX-License-Identifier: MIT

pragma solidity 0.7.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.7/VRFConsumerBase.sol";

contract AdvancedCollectible is ERC721, VRFConsumerBase {
    uint256 public tokenCounter;
    bytes32 public keyhash;
    uint256 public fee;

    uint256 public lastRandom;
    enum Trait {
        Plain,
        Halo,
        Sunglasses,
        Tattoo
    }
    mapping(uint256 => Trait) public tokenIdToTrait;
    mapping(bytes32 => address) public requestIdToSender;
    mapping(Trait => string) traitToIpfs;

    event requestedCollectible(bytes32 indexed requestId, address requester);
    event traitAssigned(uint256 indexed tokenId, Trait trait);

    constructor(
        address _vrfCoordinator,
        address _linkToken,
        bytes32 _keyHash,
        uint256 _fee
    ) VRFConsumerBase(_vrfCoordinator, _linkToken) ERC721("Testie", "TST") {
        tokenCounter = 0;
        keyhash = _keyHash;
        fee = _fee;
        traitToIpfs[
            Trait.Plain
        ] = "https://ipfs.io/ipfs/QmXjVAPoEZWNsnkdGruoT7radKSUu8PtKq4w7PDhdjN1Ds?filename=NibbledBit_plain.json";
        traitToIpfs[
            Trait.Halo
        ] = "https://ipfs.io/ipfs/QmeGrBPQSNdTeTp9nurMQZUhNThLGRiWAy4T3ZxuPWf4Ta?filename=NibbledBit_halo.json";
        traitToIpfs[
            Trait.Sunglasses
        ] = "https://ipfs.io/ipfs/QmYvf5uMHTZU4Xier2kJy5aNhzM9R4VRGgMZpsiGeM3uWa?filename=NibbledBit_sun.json";
        traitToIpfs[
            Trait.Tattoo
        ] = "https://ipfs.io/ipfs/QmfD87TWd2CLSvoMaThsVjX1pm1fCxFFx8qqKwcSebZvDP?filename=NibbledBit_tat.json";
    }

    function createCollectible() public returns (bytes32) {
        bytes32 requestId = requestRandomness(keyhash, fee);
        requestIdToSender[requestId] = msg.sender;
        emit requestedCollectible(requestId, msg.sender);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber)
        internal
        override
    {
        Trait trait = Trait(randomNumber % 4);
        uint256 newTokenId = tokenCounter;
        tokenIdToTrait[newTokenId] = trait;
        emit traitAssigned(newTokenId, trait);

        address owner = requestIdToSender[requestId];
        _safeMint(owner, newTokenId);

        _setTokenURI(tokenCounter, traitToIpfs[trait]);

        tokenCounter = tokenCounter + 1;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: caller is not owner nor approved"
        );
        _setTokenURI(tokenId, _tokenURI);
    }
}
