import json
from urllib.request import urlopen, Request

# Free, open currency API endpoint (Yahoo Finance deprecated their old endpoint)
url = 'https://api.exchangerate-api.com/v4/latest/USD'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

with urlopen(req) as response:
    source = response.read()

# json.loads parses raw bytes/string into a Python dictionary
data = json.loads(source)

# Print formatted JSON string
print(json.dumps(data, indent=2))

usd_rates = dict()

for rate_name, price in data['rates'].items():
    usd_rates[rate_name] = price
    print(f"{rate_name} --> {price}")

print(50 * float(usd_rates['EUR']))

print(50 * float(usd_rates['INR']))