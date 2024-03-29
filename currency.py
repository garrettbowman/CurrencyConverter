#second implementation of currency converter

import requests

API_KEY = "fca_live_xfI5TZyCCExiqgYc9CNISPTiAHPbHp5UCavdCXKz" 

BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY", "JPY", "INR", "GBP", "NZD", "CHF"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid currency or error fetching data")
        return None
    

while True:

    base = input("Enter the base currency (q to quit): ").upper()

    if base == "Q":
        break

    #if base not in CURRENCIES:
        #print("Invalid currency")

    data = convert_currency(base)
    if not data:
        continue
    
    del data[base]

    for ticker, value in data.items():
        print(f"{ticker}: {value}")
