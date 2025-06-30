import sys
import requests

def get_bitcoin_price() -> float:
    """Fetch the current Bitcoin price in USD from CoinDesk API."""
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        data = response.json()
        bitcoin_price = data["bpi"]["USD"]["rate_float"]
        return float(bitcoin_price)
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        sys.exit(1)