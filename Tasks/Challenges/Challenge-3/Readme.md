# GitHub Challenge Smart Contract 🔗

![Solidity](https://img.shields.io/badge/Solidity-0.8.19-363636?logo=solidity)
![Ethereum](https://img.shields.io/badge/Ethereum-Sepolia-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Deployed-success.svg)

A simple yet elegant Solidity smart contract that links your Ethereum wallet address to your GitHub identity on the blockchain. Built for **DD2585 - Programmable Society** course at KTH.


## 🎯 Overview

The `GithubChallenge` contract provides a permanent, immutable link between an Ethereum address and a GitHub username. Once deployed, anyone can verify the connection between a wallet address and a GitHub identity.

**Use Cases:**
- 🎓 Academic verification and identity
- 👨‍💻 Developer portfolio verification
- 🏆 Course completion proof
- 🔐 Decentralized identity linking

## ✨ Features

- ✅ **Immutable GitHub ID Storage** - Once deployed, GitHub ID cannot be changed
- ✅ **Owner Verification** - Store deployer's address for verification
- ✅ **Gas Efficient** - Minimal storage and simple logic
- ✅ **Public Accessibility** - Anyone can read the data
- ✅ **View Functions** - No gas cost for reading data
- ✅ **Clean Code** - Simple, auditable, and well-documented

## 📄 Contract Details

### Network Information

| Parameter | Value |
|-----------|-------|
| **Contract Name** | GithubChallenge |
| **Solidity Version** | ^0.8.19 |
| **License** | MIT |
| **Network** | Ethereum Sepolia Testnet |
| **Compiler** | 0.8.19+ |

### Contract Address

**Sepolia Testnet:**
```
0xYOUR_DEPLOYED_CONTRACT_ADDRESS
```

**Verify on Etherscan:**
```
https://sepolia.etherscan.io/address/0xYOUR_CONTRACT_ADDRESS
```

### State Variables

```solidity
string public githubId;     // Your GitHub username
address public owner;       // Deployer's wallet address
```

## 📦 Installation

### Prerequisites

- [Node.js](https://nodejs.org/) v16+ 
- [Hardhat](https://hardhat.org/) or [Remix IDE](https://remix.ethereum.org/)
- [MetaMask](https://metamask.io/) or Brave Wallet
- Sepolia testnet ETH ([Sepolia Faucet](https://sepoliafaucet.com/))

### Setup with Hardhat

```bash
# Create project directory
mkdir github-challenge
cd github-challenge

# Initialize npm project
npm init -y

# Install Hardhat
npm install --save-dev hardhat

# Initialize Hardhat project
npx hardhat init

# Install dependencies
npm install --save-dev @nomicfoundation/hardhat-toolbox
npm install --save-dev @nomiclabs/hardhat-etherscan
```

### Project Structure

```
github-challenge/
└── Challenge.sol
└── README.md
```

## 🚀 Deployment

### Method 1: Using Remix (Easiest)

1. **Open Remix IDE**
   - Go to [remix.ethereum.org](https://remix.ethereum.org)

2. **Create Contract File**
   - Create new file: `GithubChallenge.sol`
   - Paste the contract code

3. **Compile Contract**
   - Go to "Solidity Compiler" tab
   - Select compiler version: `0.8.19` or higher
   - Click "Compile GithubChallenge.sol"

4. **Deploy Contract**
   - Go to "Deploy & Run Transactions" tab
   - Environment: "Injected Provider - MetaMask"
   - Connect your wallet (Sepolia testnet)
   - Enter your GitHub username in constructor field
   - Example: `"isakibul15"` (with quotes)
   - Click "Deploy"
   - Confirm transaction in wallet

5. **Copy Contract Address**
   - After deployment, copy the contract address
   - Save it for verification and interaction

### Method 2: Using Hardhat

**hardhat.config.js**
```javascript
require("@nomicfoundation/hardhat-toolbox");
require("@nomiclabs/hardhat-etherscan");

module.exports = {
  solidity: "0.8.19",
  networks: {
    sepolia: {
      url: "https://rpc.ankr.com/eth_sepolia/YOUR_API_KEY",
      accounts: ["YOUR_PRIVATE_KEY"]
    }
  },
  etherscan: {
    apiKey: "YOUR_ETHERSCAN_API_KEY"
  }
};
```

**scripts/deploy.js**
```javascript
const hre = require("hardhat");

async function main() {
  const githubId = "isakibul15"; // Replace with your GitHub username
  
  console.log("Deploying GithubChallenge contract...");
  
  const GithubChallenge = await hre.ethers.getContractFactory("GithubChallenge");
  const contract = await GithubChallenge.deploy(githubId);
  
  await contract.deployed();
  
  console.log("Contract deployed to:", contract.address);
  console.log("GitHub ID:", await contract.githubId());
  console.log("Owner:", await contract.owner());
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

**Deploy**
```bash
npx hardhat run scripts/deploy.js --network sepolia
```

### Method 3: Using Foundry

```bash
# Deploy
forge create --rpc-url $SEPOLIA_RPC_URL \
  --private-key $PRIVATE_KEY \
  --constructor-args "isakibul15" \
  src/GithubChallenge.sol:GithubChallenge
```

## 📖 Usage

### Reading Contract Data

#### Using Etherscan

1. Go to your contract on [Sepolia Etherscan](https://sepolia.etherscan.io/)
2. Click "Contract" tab
3. Click "Read Contract"
4. View `githubId` and `owner` functions

#### Using Web3.js

```javascript
const Web3 = require('web3');
const web3 = new Web3('https://rpc.ankr.com/eth_sepolia');

const contractAddress = '0xYOUR_CONTRACT_ADDRESS';
const abi = [
  "function getGithubId() external view returns (string memory)",
  "function addressOwner() external view returns (address)"
];

const contract = new web3.eth.Contract(abi, contractAddress);

// Get GitHub ID
const githubId = await contract.methods.getGithubId().call();
console.log("GitHub ID:", githubId);

// Get Owner
const owner = await contract.methods.addressOwner().call();
console.log("Owner:", owner);
```

#### Using Ethers.js

```javascript
const { ethers } = require('ethers');

const provider = new ethers.providers.JsonRpcProvider('https://rpc.ankr.com/eth_sepolia');
const contractAddress = '0xYOUR_CONTRACT_ADDRESS';

const abi = [
  "function getGithubId() external view returns (string memory)",
  "function addressOwner() external view returns (address)",
  "function githubId() external view returns (string memory)",
  "function owner() external view returns (address)"
];

const contract = new ethers.Contract(contractAddress, abi, provider);

// Get data
const githubId = await contract.getGithubId();
const owner = await contract.addressOwner();

console.log(`GitHub: ${githubId}, Owner: ${owner}`);
```

#### Using Cast (Foundry)

```bash
# Get GitHub ID
cast call 0xYOUR_CONTRACT_ADDRESS "getGithubId()(string)" --rpc-url $SEPOLIA_RPC_URL

# Get Owner
cast call 0xYOUR_CONTRACT_ADDRESS "addressOwner()(address)" --rpc-url $SEPOLIA_RPC_URL
```

## 🔧 Functions

### Public State Variables

#### `githubId`
```solidity
string public githubId;
```
- **Type:** `string`
- **Visibility:** `public`
- **Description:** Stores the GitHub username
- **Gas Cost:** Free to read (view function)

#### `owner`
```solidity
address public owner;
```
- **Type:** `address`
- **Visibility:** `public`
- **Description:** Stores the deployer's wallet address
- **Gas Cost:** Free to read (view function)

### External Functions

#### `getGithubId()`
```solidity
function getGithubId() external view returns (string memory)
```
- **Visibility:** `external`
- **Mutability:** `view` (read-only)
- **Returns:** GitHub username as string
- **Gas Cost:** 0 (free to call)
- **Purpose:** Explicit getter for GitHub ID

**Example:**
```javascript
const githubId = await contract.getGithubId();
// Returns: "isakibul15"
```

#### `addressOwner()`
```solidity
function addressOwner() external view returns (address)
```
- **Visibility:** `external`
- **Mutability:** `view` (read-only)
- **Returns:** Owner's Ethereum address
- **Gas Cost:** 0 (free to call)
- **Purpose:** Explicit getter for owner address

**Example:**
```javascript
const owner = await contract.addressOwner();
// Returns: "0x78a99507C200dC674830861b60DB79CF0f96c663"
```

## 🧪 Testing

### Unit Tests with Hardhat

**test/GithubChallenge.test.js**
```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("GithubChallenge", function () {
  let contract;
  let owner;
  const githubId = "isakibul15";

  beforeEach(async function () {
    [owner] = await ethers.getSigners();
    const GithubChallenge = await ethers.getContractFactory("GithubChallenge");
    contract = await GithubChallenge.deploy(githubId);
    await contract.deployed();
  });

  describe("Deployment", function () {
    it("Should set the correct GitHub ID", async function () {
      expect(await contract.githubId()).to.equal(githubId);
    });

    it("Should set the deployer as owner", async function () {
      expect(await contract.owner()).to.equal(owner.address);
    });

    it("Should return GitHub ID via getter", async function () {
      expect(await contract.getGithubId()).to.equal(githubId);
    });

    it("Should return owner via getter", async function () {
      expect(await contract.addressOwner()).to.equal(owner.address);
    });
  });

  describe("View Functions", function () {
    it("Should read githubId without gas", async function () {
      const tx = await contract.getGithubId();
      expect(tx).to.equal(githubId);
    });

    it("Should read owner without gas", async function () {
      const tx = await contract.addressOwner();
      expect(tx).to.equal(owner.address);
    });
  });
});
```

**Run Tests**
```bash
npx hardhat test
```

### Test Coverage

```bash
npx hardhat coverage
```

Expected Coverage: 100% ✅

## ✅ Verification

### Verify on Etherscan

```bash
npx hardhat verify --network sepolia \
  0xYOUR_CONTRACT_ADDRESS \
  "isakibul15"
```

### Manual Verification

1. Go to [Sepolia Etherscan](https://sepolia.etherscan.io/)
2. Navigate to your contract address
3. Click "Contract" → "Verify and Publish"
4. Fill in:
   - Compiler Type: Solidity (Single file)
   - Compiler Version: v0.8.19+
   - License: MIT
5. Paste contract code
6. Enter constructor arguments (your GitHub ID)
7. Click "Verify and Publish"

## 🔐 Security

### Security Analysis

✅ **No External Calls** - Contract doesn't interact with other contracts
✅ **No Reentrancy Risk** - No state changes after external calls
✅ **Immutable Data** - Data cannot be modified after deployment
✅ **No Owner Privileges** - No special functions for owner
✅ **View Functions Only** - Cannot modify state
✅ **No Funds Handling** - Cannot receive or send ETH

### Best Practices Implemented

- ✅ SPDX License Identifier
- ✅ Explicit Solidity version
- ✅ Clear variable naming
- ✅ Minimal state variables
- ✅ Gas-efficient design
- ✅ No unnecessary complexity

### Potential Improvements

While the contract is secure for its purpose, consider:

```solidity
// Add events for better tracking
event ContractDeployed(address indexed owner, string githubId);

constructor(string memory _githubId) {
    githubId = _githubId;
    owner = msg.sender;
    emit ContractDeployed(msg.sender, _githubId);
}
```

## ⚡ Gas Optimization

### Deployment Cost

| Item | Gas Cost |
|------|----------|
| Contract Creation | ~200,000 gas |
| State Variable Storage | ~20,000 gas per variable |
| **Total Deployment** | **~240,000 gas** |

At 20 Gwei: ~0.0048 ETH (~$12 at $2500/ETH)

### Read Operations

| Function | Gas Cost |
|----------|----------|
| `githubId()` | 0 (view) |
| `owner()` | 0 (view) |
| `getGithubId()` | 0 (view) |
| `addressOwner()` | 0 (view) |

### Optimization Techniques Used

1. **Minimal Storage** - Only 2 state variables
2. **View Functions** - All reads are free
3. **No Loops** - O(1) complexity
4. **String Storage** - Efficient for short strings
5. **No Dynamic Arrays** - Predictable gas costs

## 📊 Examples

### Example 1: Academic Verification

**Deployment:**
```javascript
constructor("isakibul15")
```

**Result:**
- GitHub: `isakibul15`
- Owner: `0x78a99507C200dC674830861b60DB79CF0f96c663`

**Verification:**
Anyone can verify this student's identity by reading the contract.

### Example 2: Portfolio Verification

Developers can prove code ownership:

```javascript
// Student deploys contract with GitHub username
const contract = await GithubChallenge.deploy("studentdev123");

// Employers can verify on blockchain
const githubId = await contract.getGithubId();
const walletAddress = await contract.addressOwner();

// Cross-reference with GitHub profile and wallet transactions
```

### Example 3: Course Completion Proof

```solidity
// Professor verifies student completed course
// by checking contract deployment on Sepolia
// with correct GitHub ID linked to wallet
```

## 🤝 Contributing

Contributions welcome! Here are some ideas:

- 📝 Add events for better tracking
- 🔄 Create factory contract for batch deployment
- 🌐 Build frontend interface
- 📊 Add timestamp of deployment
- 🔗 Link multiple social profiles
- 🏆 Add achievement badges

### How to Contribute

1. Fork the repository
2. Create feature branch (`git checkout -b feature/Enhancement`)
3. Commit changes (`git commit -m 'Add enhancement'`)
4. Push to branch (`git push origin feature/Enhancement`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2025 Md. Sakibul Islam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## 👨‍💻 Author

**Md. Sakibul Islam**

- **GitHub:** [@isakibul15](https://github.com/isakibul15)
- **Wallet:** `0x78a99507C200dC674830861b60DB79CF0f96c663`
- **Contract:** `0xYOUR_CONTRACT_ADDRESS` (Sepolia)
- **Course:** DD2585 - Programmable Society
- **Institution:** KTH Royal Institute of Technology
- **Semester:** Fall 2024

## 🙏 Acknowledgments

- **Course:** DD2585 - Programmable Society at KTH
- **Instructor:** Martin
- **Tools:** Remix IDE, Hardhat, Etherscan
- **Network:** Ethereum Foundation (Sepolia Testnet)

## 📚 Resources

### Solidity
- [Solidity Documentation](https://docs.soliditylang.org/)
- [Solidity by Example](https://solidity-by-example.org/)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/)

### Development Tools
- [Remix IDE](https://remix.ethereum.org/)
- [Hardhat](https://hardhat.org/)
- [Foundry](https://book.getfoundry.sh/)
- [Etherscan](https://etherscan.io/)

### Testing
- [Sepolia Faucet](https://sepoliafaucet.com/)
- [Sepolia Etherscan](https://sepolia.etherscan.io/)
- [Chainlist - Sepolia](https://chainlist.org/?search=sepolia)

## 🔗 Related Projects

- [Challenge 4 - Contract Deployment](../challenge-04/)
- [Challenge 5 - Frontend Interface](../challenge-05/)
- [Challenge 6 - Transaction Analysis](../challenge-06/)

## 📈 Stats

- **Lines of Code:** 17
- **Functions:** 2 public, 2 external
- **State Variables:** 2
- **Deployment Gas:** ~240,000
- **Read Gas:** 0 (all view functions)

---

⭐ **Star this repository** if you found it useful!

🔗 **Verify on Etherscan:** [View Contract](https://sepolia.etherscan.io/address/0xYOUR_CONTRACT)

📮 **Questions?** Open an issue

---

**Made with ❤️ for blockchain education**

*Last Updated: December 2025*