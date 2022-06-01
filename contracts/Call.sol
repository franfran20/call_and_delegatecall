//SPDX-License-Identifier: MIT

pragma solidity 0.8.7;

contract A {
    uint256 public number;
    event Stored(address indexed sender, uint256 indexed number);

    function storeNewNumber(uint256 _newNum) public {
        number = _newNum;
        emit Stored(msg.sender, _newNum);
    }

    function retrieve() public view returns(uint256){
        return number;
    }
}

contract B {
    function callContractAStore(address _contractA, uint256 _number) public {
        (bool success, bytes memory data) = _contractA.call(abi.encodeWithSignature("storeNewNumber(uint256)", _number));
        require(success);
    }
}


//write test to show that the address who called the contract was contract B and test to show that it successfully updated!