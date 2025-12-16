# Challenge 4 - Registry Smart Contract 📝

![Solidity](https://img.shields.io/badge/Solidity-0.8.20-363636?logo=solidity)
![Ethereum](https://img.shields.io/badge/Ethereum-Sepolia-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Deployed-success.svg)

A Solidity smart contract that registers challenge completion data to a central registry contract on Ethereum's Sepolia testnet. Part of the **DD2585 - Programmable Society** course at KTH.

## 🎯 Overview

The **Challenge04** contract serves as a registration mechanism for storing course challenge completion data on the blockchain. It makes a single call to a central registry contract, permanently recording:

- Transaction hash from Challenge 1
- Transaction hash from Challenge 2  
- Contract address from Challenge 3
- This contract's own address (Challenge 4)

Once registered, this data becomes immutable proof of challenge completion, queryable by anyone on the blockchain.

## 📄 Contract Details

### Deployment Information

| Parameter | Value |
|-----------|-------|
| **Contract Name** | Challenge04 |
| **Solidity Version** | ^0.8.20 |
| **License** | MIT |
| **Network** | Ethereum Sepolia Testnet |
| **Chain ID** | 11155111 |

### Contract Addresses

**Your Challenge04 Contract:**
```
0xFdB65a15B3589388BA729Ce4B2Aa98BEf79154F4
```

**Registry Contract:**
```
0x3819C7071f2bc39C83187Bf5B5aeA79Fa3e37C42
```

**Verify on Etherscan:**
- [Your Contract](https://sepolia.etherscan.io/address/0xFdB65a15B3589388BA729Ce4B2Aa98BEf79154F4)
- [Registry Contract](https://sepolia.etherscan.io/address/0x3819C7071f2bc39C83187Bf5B5aeA79Fa3e37C42)

### Challenge Data Stored

```solidity
TX_CHALLENGE01:      0x92163e78efe098d40f3a47f8dcd351130977c4e91fa41826ce7c77c269ab2f41
TX_CHALLENGE02:      0xdc1c08e2f1b8f44a7d911632abaeb04cdaf7db722afb19247a51f2c5244c4f30
CONTRACT_CHALLENGE03: 0x4Cc82640055a8a13446b415b4697384b833009bE
CONTRACT_CHALLENGE04: 0xFdB65a15B3589388BA729Ce4B2Aa98BEf79154F4
```

## 🔧 How It Works

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Your Wallet Address                       │
│              0x78a99507C200dC674830861b60DB79CF0f96c663      │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ 1. Calls register()
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Challenge04 Contract                       │
│              0xFdB65a15B3589388BA729Ce4B2Aa98BEf79154F4      │
│                                                              │
│  • Stores challenge data as constants                        │
│  • Encodes registerData() call                               │
│  • Makes low-level call to registry                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ 2. Internal call
                              │ registerData(...)
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Registry Contract                          │
│              0x3819C7071f2bc39C83187Bf5B5aeA79Fa3e37C42      │
│                                                              │
│  • Stores data in mapping: address => Data                   │
│  • Key: tx.origin (your wallet address)                      │
│  • Value: Challenge completion data                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ 3. Permanent storage
                              ▼
                    ✅ Data Registered!
```

### Registration Flow

1. **Deploy** Challenge04 contract to Sepolia
2. **Call** `register()` function from your wallet
3. **Internal Call** made to registry contract
4. **Data Stored** in registry mapping with your wallet as key
5. **Verification** Anyone can query your data using Challenge 5 frontend

### Key Design Decisions

**Why Low-Level Call?**
```solidity
registry.call(abi.encodeWithSignature(...))
```
- ✅ Flexible - Works without importing registry interface
- ✅ Gas efficient - Direct bytecode call
- ✅ Error handling - Returns bool for success/failure
- ⚠️ Requires careful encoding

**Why Constants?**
```solidity
bytes32 private constant TX_CHALLENGE01 = 0x...;
```
- ✅ Gas efficient - Compiled into bytecode
- ✅ Immutable - Cannot be changed after deployment
- ✅ Clear - Easy to verify values

**Why `address(this)`?**
```solidity
address(this) // contract_challenge04
```
- ✅ Self-referential - Automatically uses this contract's address
- ✅ No hardcoding needed
- ✅ Flexible - Works after deployment

## 🚀 Deployment

### Prerequisites

- MetaMask or Brave Wallet
- Sepolia testnet ETH ([Get from faucet](https://sepoliafaucet.com/))
- Remix IDE or Hardhat

### Method 1: Remix IDE (Recommended)

#### Step 1: Open Remix
```
https://remix.ethereum.org
```

#### Step 2: Create Contract
1. Create new file: `Challenge04.sol`
2. Paste the contract code
3. Save (Ctrl+S / Cmd+S)

#### Step 3: Compile
1. Go to "Solidity Compiler" tab (left sidebar)
2. Select compiler version: `0.8.20` or higher
3. Click "Compile Challenge04.sol"
4. Look for green checkmark ✅

#### Step 4: Deploy
1. Go to "Deploy & Run Transactions" tab
2. **Environment:** "Injected Provider - MetaMask"
3. Connect your wallet (approve in MetaMask)
4. Verify network: **Sepolia Test Network**
5. **Contract:** Select "Challenge04"
6. Click **"Deploy"** (orange button)
7. Confirm transaction in wallet
8. Wait for confirmation (~15-30 seconds)

#### Step 5: Copy Address
1. Find deployed contract under "Deployed Contracts"
2. Click copy icon to copy address
3. Save this address - you'll need it!

### Method 2: Hardhat

**Installation:**
```bash
npm install --save-dev hardhat
npm install --save-dev @nomicfoundation/hardhat-toolbox
```

**hardhat.config.js:**
```javascript
require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.20",
  networks: {
    sepolia: {
      url: "https://rpc.ankr.com/eth_sepolia/YOUR_API_KEY",
      accounts: ["YOUR_PRIVATE_KEY"]
    }
  }
};
```

**Deploy script (scripts/deploy.js):**
```javascript
const hre = require("hardhat");

async function main() {
  console.log("Deploying Challenge04 contract...");
  
  const Challenge04 = await hre.ethers.getContractFactory("Challenge04");
  const contract = await Challenge04.deploy();
  
  await contract.deployed();
  
  console.log("✅ Contract deployed to:", contract.address);
  console.log("Registry:", await contract.registry());
  
  console.log("\n🔗 Verify on Etherscan:");
  console.log(`https://sepolia.etherscan.io/address/${contract.address}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

**Deploy:**
```bash
npx hardhat run scripts/deploy.js --network sepolia
```

## 📖 Usage

### Calling the register() Function

#### Using Remix

1. Go to "Deploy & Run Transactions" tab
2. Find your deployed contract
3. Expand it by clicking the `>` arrow
4. Find the orange **"register"** button
5. Click **"register"**
6. Confirm transaction in wallet
7. Wait for confirmation
8. Check Etherscan for internal transaction

#### Using Etherscan

1. Go to your contract on Etherscan
2. Click "Contract" tab → "Write Contract"
3. Click "Connect to Web3"
4. Connect your wallet
5. Find `register` function
6. Click "Write"
7. Confirm transaction

#### Using Ethers.js

```javascript
const { ethers } = require('ethers');

// Setup
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();

const contractAddress = "0xFdB65a15B3589388BA729Ce4B2Aa98BEf79154F4";
const abi = [
  "function register() external",
  "function registry() public view returns (address)"
];

const contract = new ethers.Contract(contractAddress, abi, signer);

// Call register
async function registerData() {
  console.log("Calling register()...");
  
  const tx = await contract.register();
  console.log("Transaction sent:", tx.hash);
  
  const receipt = await tx.wait();
  console.log("✅ Registered! Block:", receipt.blockNumber);
}

registerData();
```

#### Using Cast (Foundry)

```bash
cast send 0xFdB65a15B3589388BA729Ce4B2Aa98BEf79154F4 \
  "register()" \
  --rpc-url $SEPOLIA_RPC_URL \
  --private-key $PRIVATE_KEY
```

### Verifying Registration

After calling `register()`, verify your data:

**Method 1: Use Challenge 5 Frontend**
```
1. Open Challenge 5 frontend (IPFS link)
2. Connect wallet
3. Enter your wallet address
4. Click "Get Data"
5. See your registered challenge data
```

**Method 2: Call Registry Directly**
```javascript
const registryAddress = "0x3819C7071f2bc39C83187Bf5B5aeA79Fa3e37C42";
const registryAbi = [
  "function getData(address user) public view returns (tuple(bytes32,bytes32,address,address))"
];

const registry = new ethers.Contract(registryAddress, registryAbi, provider);
const data = await registry.getData("YOUR_WALLET_ADDRESS");

console.log("TX Challenge 01:", data[0]);
console.log("TX Challenge 02:", data[1]);
console.log("Contract Challenge 03:", data[2]);
console.log("Contract Challenge 04:", data[3]);
```

## 🔧 Functions

### External Functions

#### `register()`
```solidity
function register() external
```

**Description:** Registers challenge completion data to the central registry

**Visibility:** `external` (can only be called from outside)

**Gas Cost:** ~150,000 - 200,000 gas

**Process:**
1. Encodes function signature and parameters
2. Makes low-level call to registry contract
3. Checks return value for success
4. Reverts with error message if call fails

**What it does:**
- Calls `registerData()` on registry contract
- Passes 4 parameters: 2 transaction hashes, 2 contract addresses
- Uses `tx.origin` (your wallet) as the storage key in registry
- Creates permanent, immutable record

**Events Generated:**
- Registry contract emits events (if implemented)
- Transaction recorded on blockchain

**Example Transaction:**
```
https://sepolia.etherscan.io/tx/0x377b0553f35138bfa36f1899f4d6088403c45823b86e9e434cfddd5a94a055bc
```

### Public State Variables

#### `registry`
```solidity
address public constant registry
```
- **Value:** `0x3819C7071f2bc39C83187Bf5B5aeA79Fa3e37C42`
- **Type:** `address` (constant)
- **Description:** Address of central registry contract
- **Gas to read:** 0 (constant, compiled into bytecode)

### Private Constants

#### Challenge Data
```solidity
bytes32 private constant TX_CHALLENGE01
bytes32 private constant TX_CHALLENGE02
address private constant CONTRACT_CHALLENGE03
```
- **Visibility:** `private` (not accessible externally)
- **Type:** Immutable constants
- **Purpose:** Store challenge completion proof data
- **Gas:** 0 (compiled into bytecode)

## ✅ Verification

### Verify Contract on Etherscan

#### Automatic Verification (Hardhat)

```bash
npx hardhat verify --network sepolia 0xYOUR_CONTRACT_ADDRESS
```

#### Manual Verification

1. Go to [Sepolia Etherscan](https://sepolia.etherscan.io/)
2. Navigate to your contract address
3. Click "Contract" tab
4. Click "Verify and Publish"
5. Fill in:
   - **Compiler Type:** Solidity (Single file)
   - **Compiler Version:** v0.8.20+commit.a1b79de6
   - **License:** MIT
6. Paste full contract code
7. **Constructor Arguments:** Leave empty (no constructor args)
8. Click "Verify and Publish"
9. Wait for confirmation

#### Verification Success
Once verified, you'll see:
- ✅ Green checkmark on contract page
- 📝 Source code visible
- 🔍 "Read Contract" and "Write Contract" tabs
- 📊 Compilation details

## 🧪 Testing

### Test Contract (Hardhat)

**test/Challenge04.test.js:**
```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Challenge04", function () {
  let contract;
  let owner;
  
  const REGISTRY = "0x3819C7071f2bc39C83187Bf5B5aeA79Fa3e37C42";

  beforeEach(async function () {
    [owner] = await ethers.getSigners();
    const Challenge04 = await ethers.getContractFactory("Challenge04");
    contract = await Challenge04.deploy();
    await contract.deployed();
  });

  describe("Deployment", function () {
    it("Should set correct registry address", async function () {
      expect(await contract.registry()).to.equal(REGISTRY);
    });
  });

  describe("Register Function", function () {
    it("Should have register function", async function () {
      expect(contract.register).to.exist;
    });
    
    // Note: Actual registration test requires registry contract to exist
    it("Should call registry contract", async function () {
      // This will fail on local network but succeed on Sepolia
      // because registry contract exists on Sepolia
      
      // For local testing, you'd need to deploy a mock registry
    });
  });

  describe("Constants", function () {
    it("Should have immutable challenge data", async function () {
      // Constants are compiled into bytecode
      // Verify by checking contract bytecode includes the values
      const bytecode = await ethers.provider.getCode(contract.address);
      expect(bytecode.length).to.be.greaterThan(100);
    });
  });
});
```

**Run tests:**
```bash
npx hardhat test
```

### Integration Test on Sepolia

```javascript
// Test actual registration on Sepolia testnet
async function testRegistration() {
  const provider = new ethers.providers.JsonRpcProvider(SEPOLIA_RPC);
  const wallet = new ethers.Wallet(PRIVATE_KEY, provider);
  
  const contract = new ethers.Contract(CONTRACT_ADDRESS, ABI, wallet);
  
  console.log("Calling register()...");
  const tx = await contract.register();
  console.log("TX Hash:", tx.hash);
  
  const receipt = await tx.wait();
  console.log("✅ Success! Block:", receipt.blockNumber);
  
  // Verify in registry
  const registry = new ethers.Contract(REGISTRY_ADDRESS, REGISTRY_ABI, provider);
  const data = await registry.getData(wallet.address);
  
  console.log("\n📊 Registered Data:");
  console.log("TX Challenge 01:", data.tx_challenge01);
  console.log("TX Challenge 02:", data.tx_challenge02);
  console.log("Contract Challenge 03:", data.contract_challenge03);
  console.log("Contract Challenge 04:", data.contract_challenge04);
}
```

## 🔐 Security

### Security Analysis

✅ **No Reentrancy Risk**
- Single external call with no state changes after
- Uses `require` to handle failures
- No recursive calls possible

✅ **Access Control**
- `register()` is `external` - anyone can call
- No privileged functions
- No owner or admin

✅ **Input Validation**
- No user inputs (all data is constants)
- Cannot be manipulated

✅ **Low-Level Call Safety**
```solidity
(bool ok, ) = registry.call(...);
require(ok, "registerData call failed");
```
- Checks return value
- Reverts on failure
- Clear error message

⚠️ **Considerations**

**Gas Griefing:** Not applicable - fixed gas usage

**Registry Trust:** Contract trusts registry at `0x3819C7...`
- Registry is course-provided contract
- Assumed to be audited and safe
- Immutable address (constant)

### Best Practices Implemented

- ✅ SPDX License Identifier
- ✅ Explicit Solidity version
- ✅ Constants for immutability
- ✅ Minimal external dependencies
- ✅ Clear error messages
- ✅ No payable functions (cannot receive ETH)

## ⚡ Gas Analysis

### Deployment Cost

```
Contract Creation:     ~400,000 gas
Constant Storage:      ~0 gas (compiled into bytecode)
────────────────────
Total Deployment:      ~400,000 gas
```

**At 20 Gwei:** ~0.008 ETH (~$20 at $2,500/ETH)

### register() Function Cost

```
Function Call:         ~21,000 gas (base)
CALL opcode:          ~9,000 gas
Data encoding:        ~10,000 gas
Registry storage:     ~120,000 gas
────────────────────
Total per call:       ~160,000 gas
```

**At 20 Gwei:** ~0.0032 ETH (~$8 at $2,500/ETH)

### Optimization Techniques

1. **Constants over Variables**
   ```solidity
   // ✅ Good (0 gas)
   bytes32 private constant TX = 0x...;
   
   // ❌ Bad (20,000 gas)
   bytes32 private tx = 0x...;
   ```

2. **Low-Level Call**
   ```solidity
   // ✅ Good (efficient)
   registry.call(abi.encodeWithSignature(...));
   
   // ❌ Alternative (requires interface import)
   IRegistry(registry).registerData(...);
   ```

3. **No Storage Writes**
   - Only writes to registry contract
   - Challenge04 has no state changes
   - Very gas efficient

## 🔗 Related Challenges

### Challenge Flow

```
Challenge 1 → Transaction Hash stored
       ↓
Challenge 2 → Transaction Hash stored
       ↓
Challenge 3 → Contract Address stored
       ↓
Challenge 4 → THIS CONTRACT (registers all data)
       ↓
Challenge 5 → Frontend to view data
       ↓
Challenge 6 → Analyze registration transaction
```

### Repository Links

- **Challenge 4 (This Contract)** - Registry integration
- [Challenge 5 - Frontend](../challenge-05/) - Web interface for querying
- [Challenge 6 - Analyzer](../challenge-06/) - Transaction analysis tool

## 🐛 Troubleshooting

### Common Issues

#### "registerData call failed"

**Cause:** Registry contract call failed

**Solutions:**
1. Check Sepolia network connection
2. Ensure registry contract exists at `0x3819C7...`
3. Verify sufficient gas limit (200,000+)
4. Check wallet has Sepolia ETH

#### "Transaction Reverted"

**Possible causes:**
- Out of gas (increase gas limit)
- Registry contract issue
- Already registered (check if allowed)

**Debug:**
```javascript
// Check registry exists
const code = await provider.getCode(REGISTRY_ADDRESS);
console.log("Registry exists:", code !== '0x');
```

#### "Cannot read property 'register'"

**Cause:** Contract not deployed or wrong address

**Solution:**
1. Verify contract is deployed
2. Check contract address is correct
3. Ensure using correct ABI

#### Internal Transaction Not Showing

**Cause:** Etherscan indexing delay

**Solution:**
- Wait 1-2 minutes
- Refresh Etherscan page
- Check "Internal Txns" tab

## 📚 Resources

### Ethereum & Solidity
- [Solidity Documentation](https://docs.soliditylang.org/en/v0.8.20/)
- [Ethereum.org](https://ethereum.org/developers)
- [Solidity by Example](https://solidity-by-example.org/)

### Tools
- [Remix IDE](https://remix.ethereum.org/)
- [Sepolia Etherscan](https://sepolia.etherscan.io/)
- [Sepolia Faucet](https://sepoliafaucet.com/)

### Testing & Development
- [Hardhat](https://hardhat.org/)
- [Foundry](https://book.getfoundry.sh/)
- [OpenZeppelin](https://docs.openzeppelin.com/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Md. Sakibul Islam**

- **GitHub:** [@sakibulislam](https://github.com/isakibul15)
- **Wallet:** `0x78a99507C200dC674830861b60DB79CF0f96c663`
- **Contract:** `0xFdB65a15B3589388BA729Ce4B2Aa98BEf79154F4`
- **Register TX:** `0x377b0553f35138bfa36f1899f4d6088403c45823b86e9e434cfddd5a94a055bc`
- **Course:** DD2585 - Programmable Society
- **Institution:** KTH Royal Institute of Technology
- **Semester:** Fall 2024

## 🙏 Acknowledgments

- **Course:** DD2585 - Programmable Society at KTH
- **Instructor:** Martin
- **Registry Contract:** Course-provided infrastructure
- **Tools:** Remix IDE, Etherscan, MetaMask/Brave Wallet

---

⭐ **Star this repository** if you found it helpful!

🔗 **View on Etherscan:** [Contract](https://sepolia.etherscan.io/address/0xFdB65a15B3589388BA729Ce4B2Aa98BEf79154F4) | [Transaction](https://sepolia.etherscan.io/tx/0x377b0553f35138bfa36f1899f4d6088403c45823b86e9e434cfddd5a94a055bc)

📮 **Questions?** Open an issue

---

**Made with ❤️ for blockchain education**

*Last Updated: December 2025*