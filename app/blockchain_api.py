import requests
from config.config import ETHERSCAN_API_KEY

def fetch_wallet_data(wallet_address):
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={wallet_address}&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
