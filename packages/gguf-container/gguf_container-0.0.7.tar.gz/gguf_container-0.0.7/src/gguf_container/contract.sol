// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Base64.sol";

contract Container is ERC721 {
    address private _owner;
    address public admin;

    uint public maxSupply;
    uint public totalSupply;
    bool public isClosed;

    struct Pig {
        uint pigId;
        string name;
        uint cost;
        string image;
        bool isOwned;
    }

    mapping(uint => Pig) pigs;

    modifier ownerOnly() {
        require(msg.sender == _owner);
        _;
    }

    modifier adminOnly() {
        require(msg.sender == admin);
        _;
    }

    constructor() ERC721("container", "GGUF")
    {
        _owner = msg.sender;
    }

    function changeOwner(address newOwner) public ownerOnly {
        _owner = newOwner;
    }

    function owner() public view returns(address) {
        return _owner;
    }

    function assignAdmin(address _admin) public ownerOnly {
        admin = _admin;
    }

    function modifyCost(uint _id, uint _cost) public ownerOnly {
        require(pigs[_id].isOwned == false);
        pigs[_id].cost = _cost;
    }

    function redeem(address _to, uint _amount) public ownerOnly {
        (bool success, ) = _to.call{value: _amount}("");
        require(success);
    }

    function closeShop(bool _close) public ownerOnly {
        isClosed = _close;
    }

    function list(string memory _name, uint _cost, string memory _image) public adminOnly {
        maxSupply++;
        pigs[maxSupply] = Pig(maxSupply, _name, _cost, _image, false);
    }

    function editPig(uint _id, string memory _name, string memory _image) public adminOnly {
        require(pigs[_id].isOwned == false);
        pigs[_id].name = _name;
        pigs[_id].image = _image;
    }

    function getBalance() public view returns (uint) {
        return address(this).balance;
    }

    function getPig(uint _id) public view returns (Pig memory) {
        return pigs[_id];
    }

    function modifyPig(uint _id, string memory _name, string memory _image) public {
        require(ERC721.ownerOf(_id) == msg.sender);
        pigs[_id].name = _name;
        pigs[_id].image = _image;
    }

    function mint(uint _id) public payable {
        require(!isClosed);
        require(_id != 0);
        require(_id <= maxSupply);
        require(pigs[_id].isOwned == false);
        require(msg.value >= pigs[_id].cost);
        pigs[_id].isOwned = true;
        totalSupply++;
        _safeMint(msg.sender, _id);
    }

    function tokenURI(uint _id) override(ERC721) public view returns (string memory) {
        string memory json = Base64.encode(
            bytes(string(
                abi.encodePacked(
                    '{'
                    '"name": "', pigs[_id].name, '",',
                    '"image": "', pigs[_id].image, '"',
                    '}'
                )
            ))
        );
        return string(abi.encodePacked('data:application/json;base64,', json));
    }
}
