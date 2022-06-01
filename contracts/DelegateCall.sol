//SPDX-License-Identifier: MIT

pragma solidity 0.8.7;

contract C {
    uint256 public number;
    event Stored(address indexed sender, uint256 indexed number);

    function storeNumber(address _implementation, uint256 _number) public{
        (bool success, bytes memory data) = _implementation.delegatecall(abi.encodeWithSelector(Implementation.storeNum.selector, _number));
        require(success);
        emit Stored(msg.sender, _number);
    }

    function retrieveNumber() public view returns (uint256) {
        return number;
    }
}

contract Implementation {
    uint256 public number;

    function storeNum (uint256 _number) public{
        number = _number;
    }
}