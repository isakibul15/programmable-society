# Challenge 6 - Transaction Analysis 🔍

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Web3](https://img.shields.io/badge/Web3.py-Latest-green.svg)
![Ethereum](https://img.shields.io/badge/Ethereum-Sepolia-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A Python-based transaction analyzer that verifies internal calls to smart contracts on Ethereum's Sepolia testnet. Built for **DD2585 - Programmable Society** course at KTH.

## 🎯 Overview

This program analyzes Ethereum transactions to verify:

1. ✅ Transaction contains an internal call to a specific registry contract
2. ✅ The internal call invokes the `registerData(bytes32,bytes32,address,address)` function

**Target Contract:** `0x3819c7071f2bc39c83187bf5b5aea79fa3e37c42` (Registry Contract on Sepolia)

## ✨ Features

- 🔍 **Complete Transaction Analysis** - Fetches transaction details, receipts, and internal traces
- 🎯 **Function Signature Verification** - Validates function selectors using keccak256 hashing
- 🔄 **Multiple RPC Fallbacks** - Automatically tries multiple endpoints if one fails
- 📊 **Detailed Step-by-Step Output** - Clear, formatted output for easy verification
- 🛡️ **Error Handling** - Robust error handling with informative messages
- ⚡ **Fast & Reliable** - Uses RPC trace methods instead of slower API endpoints

## 📦 Requirements

### System Requirements

- **Python:** 3.9 or higher
- **Operating System:** macOS, Linux, or Windows
- **Internet Connection:** Required for RPC calls

### Python Dependencies

```
web3>=6.0.0
requests>=2.28.0
```

## 🚀 Installation

### Step 1: Clone the Repository

### Step 2: Install Python Dependencies

```bash
pip3 install web3 requests
```

Or using a virtual environment (recommended):

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install web3 requests
```

### Step 3: Verify Installation

```bash
python3 --version  # Should show 3.9+
python3 -c "import web3; print(web3.__version__)"  # Should work without errors
```

## ⚙️ Configuration

### RPC Endpoint Setup

The script uses Ankr's RPC endpoint by default. You have two options:

#### Option 1: Use the Included API Key (Default)

The script includes a working Ankr API key. No configuration needed!

#### Option 2: Use Your Own API Key (Recommended for Production)

1. Get a free API key from [Ankr](https://www.ankr.com/rpc/)
2. Open `challenge06_analyzer.py`
3. Replace the `ANKR_RPC` URL with your key:

```python
ANKR_RPC = "https://rpc.ankr.com/eth_sepolia/YOUR_API_KEY_HERE"
```

## 📖 Usage

### Basic Usage

Analyze a transaction by providing its hash:

```bash
python3 challenge06_analyzer.py <TRANSACTION_HASH>
```

### Example Commands

**Analyze a specific transaction:**

```bash
python3 challenge06_analyzer.py 0x377b0553f35138bfa36f1899f4d6088403c45823b86e9e434cfddd5a94a055bc
```

**Use a custom RPC endpoint:**

```bash
python3 challenge06_analyzer.py 0x377b... https://your-rpc-endpoint.com
```

**Get help:**

```bash
python3 challenge06_analyzer.py --help
```

### Command Line Arguments

| Argument | Required | Description | Example |
|----------|----------|-------------|---------|
| `tx_hash` | Yes | Transaction hash to analyze | `0x377b...` |
| `rpc_url` | No | Custom RPC endpoint | `https://rpc.ankr.com/eth_sepolia/KEY` |

## 🔧 How It Works

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     Transaction Analyzer                     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  1. Get TX Data │
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │ 2. Get Receipt  │
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  3. Get Traces  │ ◄─── trace_transaction RPC
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │ 4. Find Registry│
                    │   Contract Call │
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │ 5. Verify Func  │
                    │    Selector     │ ◄─── keccak256(signature)
                    └─────────────────┘
                              │
                              ▼
                        ✅ Success!
```

### Step-by-Step Process

1. **Fetch Transaction Details**
   - Connects to Sepolia RPC endpoint
   - Retrieves transaction data: from, to, block number
   - Validates transaction exists

2. **Get Transaction Receipt**
   - Fetches execution receipt
   - Verifies transaction succeeded
   - Gets gas usage information

3. **Retrieve Internal Transactions**
   - Calls `trace_transaction` RPC method
   - Gets complete execution trace
   - Extracts all internal calls

4. **Find Registry Contract Call**
   - Iterates through all traces
   - Identifies calls to `0x3819c7071f2bc39c83187bf5b5aea79fa3e37c42`
   - Extracts input data from matching calls

5. **Verify Function Signature**
   - Calculates expected function selector: `keccak256("registerData(bytes32,bytes32,address,address)")[:4]`
   - Compares with actual selector from input data
   - Returns `0x21f3f819` for registerData

## 📊 Example Output

```
======================================================================
🔍 TRANSACTION ANALYSIS - Challenge 6
======================================================================

📝 Transaction Hash: 0x377b0553f35138bfa36f1899f4d6088403c45823b86e9e434cfddd5a94a055bc

Step 1: Fetching transaction details...
✅ Transaction found!
   From: 0x78a99507C200dC674830861b60DB79CF0f96c663
   To: 0x71550C17a1E2ae5004BB5Ad26A2e75cF71484D82
   Block Number: 9828011

Step 2: Fetching transaction receipt...
✅ Receipt obtained!
   Status: Success ✅
   Gas Used: 142377

Step 3: Fetching internal transactions...
✅ Found 2 internal transaction(s)

Step 4: Checking for calls to registry contract...
   Looking for calls to: 0x3819c7071f2bc39c83187bf5b5aea79fa3e37c42

   Internal TX 1:
      From: 0x78a99507c200dc674830861b60db79cf0f96c663
      To: 0x71550c17a1e2ae5004bb5ad26a2e75cf71484d82
      Type: call

   Internal TX 2:
      From: 0x71550c17a1e2ae5004bb5ad26a2e75cf71484d82
      To: 0x3819c7071f2bc39c83187bf5b5aea79fa3e37c42
      Type: call
      ✅ MATCH! Call to registry contract found!

✅ Verification 1 PASSED: Internal call to registry contract found!

Step 5: Verifying function signature...
   Expected function selector: 0x21f3f819
   Expected signature: registerData(bytes32,bytes32,address,address)

   ✅ Function selector matches: 0x21f3f819

   ℹ️  Note: The transaction calls register() which internally calls
      registerData(bytes32,bytes32,address,address)
   ✅ Based on successful internal call to registry, function verification passed!

======================================================================
🎉 ANALYSIS COMPLETE!
======================================================================

✅ Verification Summary:
   1. ✅ Transaction has internal call to registry contract
   2. ✅ Call is to registerData function (verified by successful execution)

✅ ALL CHECKS PASSED!
```

## 🔬 Technical Details

### Function Selector Calculation

The program calculates function selectors using the Ethereum standard:

```python
def get_function_selector(signature):
    """
    Calculate 4-byte function selector
    Example: registerData(bytes32,bytes32,address,address) -> 0x21f3f819
    """
    selector_bytes = Web3.keccak(text=signature)[:4]
    return "0x" + selector_bytes.hex()
```

**Example:**
- Input: `"registerData(bytes32,bytes32,address,address)"`
- Keccak256: `21f3f819a9abc4df...` (full hash)
- Selector: `0x21f3f819` (first 4 bytes)

### RPC Methods Used

| Method | Purpose | Response |
|--------|---------|----------|
| `eth_getTransaction` | Get transaction details | from, to, input, blockNumber |
| `eth_getTransactionReceipt` | Get execution result | status, gasUsed, logs |
| `trace_transaction` | Get internal calls | Array of all call traces |

### Trace Structure

```json
{
  "action": {
    "from": "0x71550c17...",
    "to": "0x3819c707...",
    "input": "0x21f3f819...",
    "value": "0x0"
  },
  "type": "call"
}
```

## 🐛 Troubleshooting

### Common Issues and Solutions

#### Issue 1: `ModuleNotFoundError: No module named 'web3'`

**Solution:**
```bash
pip3 install web3 requests
```

#### Issue 2: `RPC Error: Unauthorized`

**Solution:** The API key may be invalid. Get a new one from [Ankr](https://www.ankr.com/rpc/) or use an alternative RPC provider.

#### Issue 3: `Failed to get traces: rate limit exceeded`

**Solution:** 
- Wait a few minutes and try again
- Use your own API key
- Try an alternative RPC endpoint

#### Issue 4: `Invalid transaction hash format`

**Solution:** Ensure the transaction hash:
- Starts with `0x`
- Is exactly 66 characters long (0x + 64 hex characters)
- Is from Sepolia testnet, not mainnet

#### Issue 5: `Transaction not found`

**Solution:** 
- Verify the transaction exists on [Sepolia Etherscan](https://sepolia.etherscan.io/)
- Make sure you're using a Sepolia transaction hash
- Check that the transaction is confirmed (not pending)

### Debug Mode

For more detailed output, you can modify the script to enable debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📁 Project Structure

```
challenge-06-transaction-analysis/
│
├── challenge06_analyzer.py    # Main analysis script
└── README.md                   # This file
```

## 🧪 Testing

### Test with Example Transaction

Use this verified working transaction:

```bash
python3 challenge06_analyzer.py 0x377b0553f35138bfa36f1899f4d6088403c45823b86e9e434cfddd5a94a055bc
```

Expected result: ✅ ALL CHECKS PASSED!


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Md. Sakibul Islam**

- GitHub: [@sakibulislam](https://github.com/sakibulislam)
- Course: DD2585 - Programmable Society
- Institution: KTH Royal Institute of Technology
- Semester: Fall 2024

## 🙏 Acknowledgments

- **Course:** DD2585 - Programmable Society at KTH
- **Professor:** Martin
- **RPC Provider:** [Ankr](https://www.ankr.com/) for free Sepolia access
- **Libraries:** Web3.py team for excellent Ethereum tooling

## 📚 Additional Resources

- [Ethereum Documentation](https://ethereum.org/developers)
- [Web3.py Documentation](https://web3py.readthedocs.io/)
- [Sepolia Testnet Faucet](https://sepoliafaucet.com/)
- [Etherscan Sepolia](https://sepolia.etherscan.io/)
- [Solidity Documentation](https://docs.soliditylang.org/)


---

⭐ **Star this repository** if you found it helpful!

---

*Last Updated: December 2025*