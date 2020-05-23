#imports
import requests
import sys

#mac address api-endpoint
API_ENDPOINT = 'https://api.macaddress.io/v1'

#input parameters for get request:
#API Key for mac macaddress
APIKEY = "at_z7i9dbzdYrwBMSWoXpgtVz6cSdHmR"
#MAC address to search. Mac address is provided my CMD arg
MACADDRESS = sys.argv[1]
#Output format. To meet requirements, hardcoding as 'vendor'.
#Although, can change to json and parse more information from result
OUTPUTFORMAT = "vendor"

#params dictionary as parameters sent to API
PARAMS = {
    'apiKey': APIKEY,
    'search': MACADDRESS,
    'output': OUTPUTFORMAT
}


response = requests.get(API_ENDPOINT, params=PARAMS)

print("Vendor name: " + response.text + "\n")
