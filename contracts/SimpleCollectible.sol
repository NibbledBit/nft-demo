// SPDX-License-Identifier: MIT

pragma solidity 0.7.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleCollectible is ERC721 {
    uint256 public tokenCounter;

    //build token
    constructor() public ERC721("Nibbles", "IDT") {
        tokenCounter = 0;
    }

    function createCollectible(string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 newTokenId = tokenCounter;
        _safeMint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        tokenCounter += 1;
        return newTokenId;
    }
}
