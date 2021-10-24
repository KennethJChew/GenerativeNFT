// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter public _tokenId;
    event NftMinted(uint256 mintedNftId);

    // TODO Set owner
    constructor() ERC721("TEST", "TST") {
        // _tokenId = 0;
    }

    // Returns the NFT ID
    function createNFT(address minter, string memory tokenURI)
        public
        returns (uint256)
    {
        /**
        Steps to mint NFT.
        1. increment tokenId
        2. set tokenID of the NFT to be created to the incremented tokenID counter
        3. mint NFT with the updated token ID to the minter's address
        4. get the URI of the generated image
        5. Update tokenURI
         */
        _tokenId.increment();
        uint256 newNftId = _tokenId.current();
        _safeMint(minter, newNftId);
        _setTokenURI(newNftId, tokenURI);
        emit NftMinted(newNftId);

        return newNftId;
    }

    function reRoll() public {
        /**
        TODO - allow minter to reroll and update URI of the NFT

         */
    }
}
