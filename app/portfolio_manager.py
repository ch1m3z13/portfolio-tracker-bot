def format_wallet_data(wallet_data):
    if wallet_data and "result" in wallet_data:
        balance = int(wallet_data["result"]) / (10 ** 18)  # Convert Wei to ETH
        return f"Wallet Balance: {balance:.4f} ETH"
    return "Unable to fetch wallet data!"
