# Challenge 5 - Blockchain Registry Frontend 🌐

![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Ethers.js](https://img.shields.io/badge/Ethers.js-2535a0?logo=ethereum&logoColor=white)
![IPFS](https://img.shields.io/badge/IPFS-65C2CB?logo=ipfs&logoColor=white)
![Ethereum](https://img.shields.io/badge/Ethereum-Sepolia-purple.svg)

A decentralized web frontend for interacting with the Challenge04 registry smart contract on Ethereum's Sepolia testnet. Deployed on IPFS for true decentralization. Built for **DD2585 - Programmable Society** course at KTH.

## 🎯 Overview

This frontend application provides a user-friendly interface to interact with the Challenge04 registry smart contract. Users can:

1. **View All Registered Addresses** - See all students who have registered their challenge data
2. **Query Specific Address Data** - Look up challenge completion data for any registered address
3. **Connect Wallet** - Seamlessly connect Brave Wallet or MetaMask
4. **Verify on Blockchain** - All data is fetched directly from the Sepolia blockchain

**Registry Contract:** `0x3819C7071f2bc39C83187Bf5B5aeA79Fa3e37C42`

## ✨ Features

### Core Functionality
- 🔍 **Get All Registered Addresses** - Fetch complete list of registered students
- 📊 **Query Individual Data** - View challenge data for specific addresses
- 💼 **Multi-Wallet Support** - Compatible with Brave Wallet, MetaMask, and other Web3 wallets
- ⚡ **Real-time Data** - Fetches live data directly from blockchain

### User Experience
- ✅ **One-Click Connection** - Easy wallet connection with modal selector
- 🎯 **Clear Status Indicators** - Always know your connection status
- 🌙 **Modern Design** - Gradient backgrounds, smooth animations, card layouts
- ⚠️ **Error Handling** - Clear error messages and troubleshooting tips
- 🔐 **Privacy First** - No data collection, fully client-side

### Technical Features
- 🚀 **Pure Frontend** - No backend required, runs entirely in browser
- 📦 **Single HTML File** - Easy to deploy and maintain
- 🌐 **IPFS Hosted** - Truly decentralized hosting
- 🔌 **Web3 Integration** - Uses ethers.js v5 for blockchain interaction
- 🔄 **Fallback Providers** - Multiple RPC endpoints for reliability
- 💾 **No Local Storage** - Respects Claude.ai artifact restrictions

## 🌍 Live Demo

### IPFS Deployment
- IPFS.io: `https://ipfs.io/ipfs/bafkreicmturww5kpdmtjerlsiuojkblczyn4dcxmhzqznqr634hheqsbai`

### Local Demo
```bash
# Simply open the HTML file in your browser
open index.html
# or
python3 -m http.server 8000
# Then visit: http://localhost:8000
```

## 🛠️ Technologies

### Frontend Stack
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with gradients, animations, flexbox
- **JavaScript (ES6+)** - Async/await, modern syntax
- **Ethers.js v5** - Ethereum JavaScript library

### Blockchain
- **Network:** Ethereum Sepolia Testnet
- **Chain ID:** 11155111
- **Contract:** Registry smart contract
- **ABI:** Minimal ABI for read-only functions

### Hosting
- **IPFS** - Decentralized file storage
- **Pinata** - IPFS pinning service (free tier)

### Web3 Wallets
- Brave Wallet (Native browser wallet)
- Any Web3-compatible wallet

## 📦 Installation

### Prerequisites

No installation required! Just need:
- Modern web browser (Chrome, Brave, Firefox, Safari)
- Web3 wallet (Brave Wallet)
- Internet connection

### Setup for Local Development

1. **Clone the repository**
```bash
git clone https://github.com/isakibul15/challenge-05-frontend.git
cd challenge-05-frontend
```

2. **Open in browser**
```bash
# Option 1: Direct file open
open index.html

# Option 2: Local server (recommended)
python3 -m http.server 8000
# Visit: http://localhost:8000

# Option 3: VS Code Live Server
# Install "Live Server" extension
# Right-click index.html → Open with Live Server
```

3. **Configure wallet**
   - Install Brave Wallet or MetaMask
   - Switch to Sepolia Testnet
   - Get test ETH from [Sepolia Faucet](https://sepoliafaucet.com/)

## 📖 Usage

### Step 1: Connect Your Wallet

1. Open the application in your browser
2. Click **"Connect Wallet"** button
3. Choose your wallet from the modal:
   - 🦁 **Brave Wallet** (Recommended if using Brave browser)
   - 🦊 **MetaMask**
4. Approve the connection in your wallet popup
5. Wait for confirmation

**Expected Result:**
```
✅ Connected (Brave): 0x78a9...c663
```

### Step 2: View All Registered Addresses

1. Click **"Get All Addresses"** button
2. Wait for data to load (1-2 seconds)
3. View the list of all registered addresses

**What You'll See:**
- Total number of registered addresses
- Each address displayed in a card
- "View Data" button for each address

### Step 3: Query Specific Address Data

**Method 1: From Address List**
1. Click "View Data" on any address card
2. Data will automatically populate

**Method 2: Manual Entry**
1. Copy an Ethereum address
2. Paste into the "Query Address Data" input field
3. Click **"Get Data"** button

**Data Displayed:**
- TX Challenge 01 (transaction hash)
- TX Challenge 02 (transaction hash)
- Contract Challenge 03 (contract address)
- Contract Challenge 04 (contract address)

### Step 4: Disconnect (Optional)

1. Click **"Disconnect Wallet"** button
2. Your wallet will be disconnected
3. All displayed data will be cleared

## 🔗 Smart Contract Integration

### Contract Details

```javascript
// Registry Contract Address
const REGISTRY_ADDRESS = "0x3819C7071f2bc39C83187Bf5B5aeA79Fa3e37C42";

// Network
const SEPOLIA_CHAIN_ID = "0xaa36a7"; // 11155111 in hex
```

### Contract ABI

```javascript
const REGISTRY_ABI = [
    "function getRegisteredAddresses() public view returns (address[])",
    "function getData(address user) public view returns (tuple(bytes32 tx_challenge01, bytes32 tx_challenge02, address contract_challenge03, address contract_challenge04))"
];
```

### Read Methods

#### 1. getRegisteredAddresses()
```javascript
const addresses = await contract.getRegisteredAddresses();
// Returns: array of Ethereum addresses
```

#### 2. getData(address)
```javascript
const data = await contract.getData(userAddress);
// Returns: tuple with challenge data
```

### Data Structure

```javascript
{
    tx_challenge01: "0x92163e78...",      // bytes32
    tx_challenge02: "0xdc1c08e2...",      // bytes32
    contract_challenge03: "0x4Cc82640...", // address
    contract_challenge04: "0xFdB65a15..."  // address
}
```

## 🚀 Deployment on IPFS

### Using Pinata (Recommended)

#### Step 1: Sign Up
1. Go to [Pinata.cloud](https://pinata.cloud)
2. Create free account
3. Verify email

#### Step 2: Upload File
1. Click **"Upload"** → **"File"**
2. Select `index.html`
3. Name it: "Challenge05-Frontend"
4. Click **"Upload"**

#### Step 3: Get IPFS Link
After upload, you'll receive a CID (Content Identifier):
```
QmYwAPJzv5CZsnA625s3Xf2nemtYgPpHdWEz79ojWnPbdG
```

Your file is now accessible at:
```
https://ipfs.io/ipfs/YOUR_CID
```

#### Step 4: Test Deployment
1. Open the IPFS URL in browser
2. Connect wallet
3. Test all functionality
4. Verify on different devices


## 🏗️ Architecture

### Application Flow

```
┌─────────────────────────────────────────────────────────┐
│                   User Interface (HTML)                  │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│              Wallet Connection (ethers.js)               │
│  ┌──────────────────┐         ┌──────────────────┐      │
│  │  Brave Wallet    │   OR    │    MetaMask      │      │
│  └──────────────────┘         └──────────────────┘      │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│           Web3 Provider (window.ethereum)                │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│              Sepolia RPC Endpoint                        │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│         Registry Smart Contract (0x3819c707...)          │
│  ┌────────────────────────────────────────────┐         │
│  │  getRegisteredAddresses()                  │         │
│  │  getData(address)                          │         │
│  └────────────────────────────────────────────┘         │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│              Display Data to User                        │
└─────────────────────────────────────────────────────────┘
```

### Component Structure

```javascript
// 1. Configuration
const REGISTRY_ADDRESS = "...";
const REGISTRY_ABI = [...];

// 2. Wallet Management
connectWallet()
disconnectWallet()
showWalletModal()
selectWallet(type)

// 3. Data Fetching
getRegisteredAddresses()
getDataForAddress(address)

// 4. UI Updates
displayAddresses(addresses)
displayData(data)
showError(message)
```

## 🌐 Browser Compatibility

### Supported Browsers

| Browser | Version | Support | Notes |
|---------|---------|---------|-------|
| Brave | Latest | ✅ Full | Native wallet support |


### Requirements
- JavaScript enabled
- Web3 wallet installed
- Popup windows allowed
- Internet connection

## 🐛 Troubleshooting

### Common Issues

#### Issue 1: "Please connect your wallet"
**Problem:** Wallet not connecting

**Solutions:**
- Ensure wallet extension is installed and enabled
- Check if wallet is unlocked
- Try refreshing the page
- Switch to Sepolia network manually

#### Issue 2: "Wrong Network"
**Problem:** Connected to wrong network

**Solutions:**
```
1. Open wallet
2. Click network dropdown
3. Select "Sepolia Test Network"
4. Refresh page
```

#### Issue 3: "No wallets detected"
**Problem:** Modal shows no wallets

**Solutions:**
- Install Brave Wallet or MetaMask
- Enable the extension
- Reload the page
- Try in Brave browser for native wallet

#### Issue 4: "No data found for this address"
**Problem:** Address shows no data

**Cause:** Address hasn't registered yet

**Solution:** 
- Verify the address is correct
- Check if you've called `register()` on Challenge04 contract
- Try another address from the registered list

#### Issue 5: "Transaction not found"
**Problem:** Can't fetch transaction data

**Solutions:**
- Verify transaction hash is correct
- Check on [Sepolia Etherscan](https://sepolia.etherscan.io/)
- Wait for transaction confirmation

### Debug Mode

Open browser console (F12) to see:
- Connection status
- Contract calls
- Error messages
- Network info

## 📁 Project Structure

```
challenge-05-frontend/
│
├── index.html                 # Main application file
└──README.md                  # This file

```

## 💻 Development

### Local Development Setup

```bash
# Clone repository
git clone https://github.com/isakibul15/challenge-05-frontend.git
cd challenge-05-frontend

# Start local server
python3 -m http.server 8000

# Open in browser
open http://localhost:8000
```

### Making Changes

1. Edit `index.html`
2. Save changes
3. Refresh browser (Cmd+R / Ctrl+R)
4. Test thoroughly

### Testing Checklist

- [ ] Wallet connection works
- [ ] Network switching prompts correctly
- [ ] Get All Addresses displays data
- [ ] Query Address Data works
- [ ] Error messages show properly
- [ ] Disconnect wallet clears data
- [ ] Mobile responsive design works
- [ ] All buttons are functional

### Code Style

- Use consistent indentation (2 spaces)
- Add comments for complex logic
- Keep functions small and focused
- Use descriptive variable names
- Handle errors gracefully


### How to Contribute

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Md. Sakibul Islam**

- GitHub: [@isakibul15](https://github.com/isakibul15)
- Wallet: `0x78a99507C200dC674830861b60DB79CF0f96c663`
- Course: DD2585 - Programmable Society
- Institution: KTH Royal Institute of Technology
- Semester: Fall 2024

## 🙏 Acknowledgments

- **Course:** DD2585 - Programmable Society at KTH
- **Professor:** Martin
- **IPFS Hosting:** [Pinata](https://pinata.cloud) for free tier
- **Libraries:** Ethers.js team for excellent Web3 tooling
- **CDN:** Cloudflare for reliable ethers.js hosting

## 📚 Resources

### Ethereum Development
- [Ethereum.org](https://ethereum.org/developers)
- [Ethers.js Documentation](https://docs.ethers.org/v5/)
- [Solidity Documentation](https://docs.soliditylang.org/)

### IPFS
- [IPFS Documentation](https://docs.ipfs.io/)
- [Pinata Guide](https://docs.pinata.cloud/)
- [IPFS Desktop](https://docs.ipfs.io/install/ipfs-desktop/)

### Sepolia Testnet
- [Sepolia Faucet](https://sepoliafaucet.com/)
- [Sepolia Etherscan](https://sepolia.etherscan.io/)
- [Chainlist - Sepolia](https://chainlist.org/?search=sepolia)

### Web3 Wallets
- [Brave Wallet Guide](https://brave.com/wallet/)
- [MetaMask Documentation](https://docs.metamask.io/)

## 🔗 Related Projects

- [Challenge 6 - Transaction Analysis](../challenge-06/) - Transaction analyzer

## 📊 Stats

- **Lines of Code:** ~600
- **File Size:** ~25KB (unminified)
- **Load Time:** < 1 second
- **Dependencies:** 1 (ethers.js via CDN)

---

⭐ **Star this repository** if you found it helpful!

🌐 **Live Demo:** [View on IPFS](https://ipfs.io/ipfs/bafkreicmturww5kpdmtjerlsiuojkblczyn4dcxmhzqznqr634hheqsbai)

📮 **Questions?** Open an issue

---

**Made with ❤️ for DD2585 - Programmable Society @ KTH**

*Last Updated: December 2025*