#imports
import requests
import sys
import re

#in case user does not provide a cmd arg
if (len(sys.argv) == 2):
    #capture command line argument and validate that it is a MAC ADDRESS
    macAddress = sys.argv[1]
    if re.match('([a-fA-F0-9]{2}[:|\-]?){6}$', macAddress):
        #mac address api-endpoint
        API_ENDPOINT = 'https://api.macaddress.io/v1'

        ##input parameters for get request:
        #My API Key for macaddress api
        APIKEY = "at_z7i9dbzdYrwBMSWoXpgtVz6cSdHmR"

        #Output format. To meet requirements, initializing as 'vendor'.
        #Although, can change to 'json' and parse more information from API call
        OUTPUTFORMAT = "vendor"

        #PARAMS dictionary as parameters sent to API
        PARAMS = {
            'apiKey': APIKEY,
            'search': macAddress,
            'output': OUTPUTFORMAT
        }
        response = requests.get(API_ENDPOINT, params=PARAMS)
        print(response.text)
    else:
        #user did not provide a valid cmd arg
        print("MAC address is not in valid format. Please input a MAC address without spaces as command line argument")
else:
    #user did not provide a valid cmd arg
    print("Please input a MAC address without spaces as command line argument")
