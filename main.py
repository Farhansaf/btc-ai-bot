import requests

def get_btc_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        print("DEBUG RESPONSE:", data)

        if "price" not in data:
            return None

        return float(data["price"])

    except Exception as e:
        print("ERROR:", e)
        return None


price = get_btc_price()

if price:
    print("BTC Price:", price)
else:
    print("Price fetch failed")
