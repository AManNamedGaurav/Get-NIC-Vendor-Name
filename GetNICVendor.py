#imports
import requests
import sys

#in case user does not provide a cmd arg
if (len(sys.argv) == 2):
    #mac address api-endpoint
    API_ENDPOINT = 'https://api.macaddress.io/v1'

    ##input parameters for get request:
    #My API Key for mac macaddress
    APIKEY = "at_z7i9dbzdYrwBMSWoXpgtVz6cSdHmR"
    #MAC address to search. Mac address is provided my CMD arg
    MACADDRESS = sys.argv[1]
    #Output format. To meet requirements, initializing as 'vendor'.
    #Although, can change to 'json' and parse more information from API call
    OUTPUTFORMAT = "vendor"

    #PARAMS dictionary as parameters sent to API
    PARAMS = {
        'apiKey': APIKEY,
        'search': MACADDRESS,
        'output': OUTPUTFORMAT
    }
    response = requests.get(API_ENDPOINT, params=PARAMS)
    print(response.text)
else:
    #user did not provide a valid cmd arg
    print("Please input a MAC address without spaces as command line argument")
