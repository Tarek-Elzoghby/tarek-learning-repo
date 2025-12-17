import sys
import requests



def main():
    #specify as a command-line argument the number of Bitcoins
    try:
        num_bitcoin = float(sys.argv[1])
    #If the argument cannot be converted to a float exit the program.
    except ValueError:
        print("Erorr!, the program expects a float number in the command line")
        sys.exit()
    except IndexError:
        print("Erorr!, the program expects a float number in the command line")
        sys.exit()
    #Queries the API for the CoinCap Bitcoin Price Index at rest.
    try:
        r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=YOUR_API_KEY_HERE")
    except requests.RequestException:
        print("sorry, something went wrong") 
        sys.exit()
    #returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. 
    price = float(r.json()['data']['priceUsd'])
    value = num_bitcoin * price

    #Outputs the current cost of 𝑛 Bitcoins in USD to four decimal places,
    print(f"${value:,.4f}")


main()
