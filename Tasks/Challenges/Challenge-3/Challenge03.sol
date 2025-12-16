// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract GithubChallenge {
    string public githubId;
    address public owner;
    
    constructor(string memory _githubId) {
        githubId = _githubId;
        owner = msg.sender;
    }
    
    function getGithubId() external view returns (string memory) {
        return githubId;
    }
    
    function addressOwner() external view returns (address) {
        return owner;
    }
}