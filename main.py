import requests
import json
import os

FILE = "last_signal.txt"

def get_btc_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(url).json()
    return float(data["price"])

def generate_signal(price):
    if price % 2 == 0:
        return "BUY"
    else:
        return "SELL"

price = get_btc_price()
signal = generate_signal(price)

print("BTC Price:", price)
print("Signal:", signal)

# last signal store karo
last = ""
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        last = f.read()

# agar signal change hua to update
if signal != last:
    print("📢 NEW SIGNAL DETECTED!")
    with open(FILE, "w") as f:
        f.write(signal)
else:
    print("No change in signal")
