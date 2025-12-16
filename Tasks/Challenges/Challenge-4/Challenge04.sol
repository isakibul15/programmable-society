// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Challenge04 {
    // Address of the their chal registry contract
    address public constant registry = 0x3819C7071f2bc39C83187Bf5B5aeA79Fa3e37C42;

    // Given constants
    bytes32 private constant TX_CHALLENGE01 =
        0x92163e78efe098d40f3a47f8dcd351130977c4e91fa41826ce7c77c269ab2f41;

    bytes32 private constant TX_CHALLENGE02 =
        0xdc1c08e2f1b8f44a7d911632abaeb04cdaf7db722afb19247a51f2c5244c4f30;

    address private constant CONTRACT_CHALLENGE03 =
        0x4Cc82640055a8a13446b415b4697384b833009bE;

    constructor() {
    }

    function register() external {
        (bool ok, ) = registry.call(
            abi.encodeWithSignature(
                "registerData(bytes32,bytes32,address,address)",
                TX_CHALLENGE01,
                TX_CHALLENGE02,
                CONTRACT_CHALLENGE03,
                address(this) // contract_challenge04
            )
        );
        require(ok, "registerData call failed");
    }
}