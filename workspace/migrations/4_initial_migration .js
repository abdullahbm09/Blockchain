var Migrations = artifacts.require("./Arduino.sol");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
};
