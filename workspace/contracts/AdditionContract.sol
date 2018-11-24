pragma solidity ^0.4.18;

contract AdditionContract {
  uint public state = 0;

  function add(uint value1) public {
    state = value1;
  }

  function getState() public constant returns (uint) {
      return state;
  }
}
