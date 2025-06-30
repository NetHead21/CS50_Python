import sys
import requests

def get_bitcoin_price() -> float:
    """Fetch the current Bitcoin price in USD from CoinDesk API."""
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"