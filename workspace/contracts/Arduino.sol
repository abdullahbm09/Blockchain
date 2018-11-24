pragma solidity ^0.4.18;

contract Arduino {
    uint public state;
function input1(uint value) public{

        if(value <= 50) {
          state = 1;
        } else if (value >= 100 ) {
          state = 0; 
        }
}
function getState() public constant returns (uint) {
      return state;
  }
}

