var Migrations = artifacts.require("./Greeter.sol");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
};
