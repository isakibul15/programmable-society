#!/usr/bin/env python3
"""
Challenge 6: Transaction Analysis using trace_transaction
Analyzes internal transactions using debug-enabled RPC endpoints
"""

import sys
import json
import requests
from web3 import Web3

# Registry contract and expected function
REGISTRY_CONTRACT = "0x3819c7071f2bc39c83187bf5b5aea79fa3e37c42"
EXPECTED_FUNCTION_SIG = "registerData(bytes32,bytes32,address,address)"

# Debug-enabled RPC endpoints
DEBUG_RPC_URLS = [
    "https://rpc.ankr.com/eth_sepolia/7d2ecae2021d16ed872c18c4cfb8c3f745a782dacbf3b627ef86925b494a8463",  # Your Ankr API key
    "https://ethereum-sepolia-rpc.publicnode.com",  # Public Node (may support debug)
    "https://sepolia.gateway.tenderly.co",  # Tenderly
    "https://rpc2.sepolia.org",  # Backup
]

def get_function_selector(signature):
    """Calculate 4-byte function selector with 0x prefix"""
    selector_bytes = Web3.keccak(text=signature)[:4]
    return "0x" + selector_bytes.hex()  # Ensure 0x prefix

def trace_transaction(rpc_url, tx_hash):
    """Call trace_transaction RPC method"""
    payload = {
        "jsonrpc": "2.0",
        "method": "trace_transaction",
        "params": [tx_hash],
        "id": 1
    }
    
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(rpc_url, json=payload, headers=headers, timeout=20)
        data = response.json()
        
        if "error" in data:
            error_msg = data['error'].get('message', 'Unknown')
            
            # Try alternative debug method if trace_transaction fails
            if "not found" in error_msg.lower() or "unsupported" in error_msg.lower():
                return try_debug_trace(rpc_url, tx_hash)
            
            return None, f"RPC Error: {error_msg}"
        
        if "result" in data:
            return data["result"], None
        
        return None, "No result in response"
        
    except Exception as e:
        return None, str(e)

def try_debug_trace(rpc_url, tx_hash):
    """Try alternative debug_traceTransaction method"""
    payload = {
        "jsonrpc": "2.0",
        "method": "debug_traceTransaction",
        "params": [tx_hash, {"tracer": "callTracer"}],
        "id": 1
    }
    
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(rpc_url, json=payload, headers=headers, timeout=20)
        data = response.json()
        
        if "error" in data:
            return None, f"Debug method also failed: {data['error'].get('message', 'Unknown')}"
        
        if "result" in data:
            # Convert debug_traceTransaction format to trace_transaction format
            result = data["result"]
            traces = convert_debug_to_trace(result)
            return traces, None
        
        return None, "No result from debug method"
        
    except Exception as e:
        return None, str(e)

def convert_debug_to_trace(debug_result):
    """Convert debug_traceTransaction result to trace_transaction format"""
    traces = []
    
    def extract_calls(call_data, trace_list):
        """Recursively extract calls from debug trace"""
        if not call_data:
            return
        
        trace = {
            "action": {
                "from": call_data.get("from", ""),
                "to": call_data.get("to", ""),
                "input": call_data.get("input", ""),
                "value": call_data.get("value", "0x0")
            },
            "type": call_data.get("type", "call")
        }
        trace_list.append(trace)
        
        # Process nested calls
        if "calls" in call_data:
            for nested_call in call_data["calls"]:
                extract_calls(nested_call, trace_list)
    
    extract_calls(debug_result, traces)
    return traces

def analyze_trace(traces):
    """Analyze traces to find internal call to registry"""
    if not traces:
        return False, "No traces found"
    
    expected_selector = get_function_selector(EXPECTED_FUNCTION_SIG)
    
    print(f"\n{'='*70}")
    print(f"Analyzing {len(traces)} trace(s)...")
    print(f"{'='*70}\n")
    
    for idx, trace in enumerate(traces):
        action = trace.get("action", {})
        trace_type = trace.get("type", "")
        
        from_addr = action.get("from", "").lower()
        to_addr = action.get("to", "").lower()
        input_data = action.get("input", "")
        
        print(f"Trace {idx + 1}:")
        print(f"  Type: {trace_type}")
        print(f"  From: {action.get('from', 'N/A')}")
        print(f"  To: {action.get('to', 'N/A')}")
        
        # Check if this is a call to the registry contract
        if to_addr == REGISTRY_CONTRACT.lower():
            print(f"  ✅ MATCH: Call to registry contract!")
            
            # Check function signature
            if len(input_data) >= 10:
                function_selector = input_data[:10].lower()  # e.g., "0x21f3f819"
                expected_lower = expected_selector.lower()   # e.g., "0x21f3f819"
                
                print(f"  Function Selector: {function_selector}")
                print(f"  Expected Selector: {expected_lower}")
                
                if function_selector == expected_lower:
                    print(f"  ✅ MATCH: Function is registerData!")
                    return True, "Found internal call to registerData"
                else:
                    print(f"  ❌ Function selector mismatch")
                    print(f"     Got: {function_selector}")
                    print(f"     Expected: {expected_lower}")
            else:
                print(f"  ⚠️  Input data too short")
        
        print()
    
    return False, "No matching internal call found"

def main():
    """Main entry point"""
    print("\n" + "="*70)
    print("Challenge 6 - Transaction Trace Analyzer")
    print("Uses trace_transaction RPC method")
    print("="*70)
    
    # Get arguments
    if len(sys.argv) < 2:
        print("\n❌ Usage: python3 challenge06_trace.py <tx-hash> [rpc-url]")
        print("\nExample:")
        print("  python3 challenge06_trace.py 0x377b...")
        print("  python3 challenge06_trace.py 0x377b... https://rpc.ankr.com/eth_sepolia")
        sys.exit(1)
    
    tx_hash = sys.argv[1]
    
    # Validate tx hash
    if not tx_hash.startswith('0x') or len(tx_hash) != 66:
        print("\n❌ Invalid transaction hash format!")
        return
    
    # Get RPC URL
    if len(sys.argv) >= 3:
        rpc_urls = [sys.argv[2]]
    else:
        rpc_urls = DEBUG_RPC_URLS
    
    print(f"\n📝 Transaction Hash: {tx_hash}")
    print(f"🎯 Target Contract: {REGISTRY_CONTRACT}")
    print(f"🔧 Expected Function: {EXPECTED_FUNCTION_SIG}\n")
    
    # Try each RPC endpoint
    traces = None
    working_rpc = None
    
    for rpc_url in rpc_urls:
        print(f"Trying RPC: {rpc_url}")
        traces, error = trace_transaction(rpc_url, tx_hash)
        
        if traces:
            working_rpc = rpc_url
            print(f"✅ Successfully retrieved traces!\n")
            break
        else:
            print(f"❌ Failed: {error}\n")
    
    if not traces:
        print("="*70)
        print("❌ FAILED: Could not retrieve traces from any RPC endpoint")
        print("="*70)
        print("\n💡 Solutions:")
        print("  1. Use a debug-enabled RPC (like Alchemy, Quicknode)")
        print("  2. Run your own Sepolia node with --http.api=debug,trace")
        print("  3. Try: https://rpc.ankr.com/eth_sepolia")
        print("  4. Try: https://sepolia.gateway.tenderly.co")
        print("\n📝 Manual verification:")
        print(f"  Check internal transactions at:")
        print(f"  https://sepolia.etherscan.io/tx/{tx_hash}#internal")
        return
    
    print(f"✅ Connected to: {working_rpc}")
    
    # Analyze traces
    found, message = analyze_trace(traces)
    
    # Final result
    print("\n" + "="*70)
    if found:
        print("🎉 ANALYSIS COMPLETE - SUCCESS!")
        print("="*70)
        print("\n✅ Verification Summary:")
        print(f"  1. ✅ Transaction has internal call to {REGISTRY_CONTRACT}")
        print(f"  2. ✅ Call is to {EXPECTED_FUNCTION_SIG}")
        print("\n✅ ALL CHECKS PASSED!")
    else:
        print("❌ ANALYSIS COMPLETE - FAILED")
        print("="*70)
        print(f"\n❌ Result: {message}")
        print(f"\n💡 The transaction may not have the expected internal call,")
        print(f"   or the traces are incomplete.")
    
    print("\n" + "="*70 + "\n")

if __name__ == "__main__":
    main()