import requests # to make https request
import sys # to haldle command_line arguments

if len(sys.argv) !=2:
    sys.exit("Missing command-line argument")

try:
    bitcoin = float(sys.argv[1])

except ValueError:
    sys.exit("Command-line argument is not a number")

url = "https://rest.coincap.io/v3/assets/bitcoin" #  CoinCap API to get Bitcoin price
headers = {
    "Authorization": "Bearer 0944621b45ce907b4bd9521557a03170ba66a48b1f8a1a39c080d4f545f73728"

}
try:
    response = requests.get(url, headers=headers) # Send GET request
    response.raise_for_status()  # Check if the request was successful
    data = response.json()
     # Extract the Bitcoin price in USD from the response data
    price = float(data["data"]["priceUsd"])

except requests.RequestException:
    sys.exit("Error fetching data from CoinCap")
cost = bitcoin * price
print(f"${cost:,.4f}")

