#imports
import requests
import sys
import re
import config

#calls mac address api to get vendor name and return it
def retrieveNICVendor(macAddress):
    #mac address api-endpoint
    API_ENDPOINT = 'https://api.macaddress.io/v1'

    ##input parameters for get request:
    #My API Key for macaddress api. probably should hide this somehow
    APIKEY = config.API_KEY

    #Output format. To meet requirements, initializing as 'vendor'.
    #Although, can change to 'json' and parse more information from API call
    OUTPUTFORMAT = "vendor"

    PARAMS = {
        'apiKey': APIKEY,
        'search': macAddress,
        'output': OUTPUTFORMAT
    }
    response = requests.get(API_ENDPOINT, params=PARAMS)
    return response.text

#determines if passed in string is in valid mac address format
def isValidMacAddress(x):
    #return true if parameter matches regex for mac addresses
    if re.match('([a-fA-F0-9]{2}[:|\-]?){6}$', x):
        return True
    else:
        return False

#gets the command line argument only if there is one. else returns None
def getMacAddressFromCMD():
    #enforces exactly 1 command line argument
    if (len(sys.argv) == 2):
        #capture command line argument and return
        return sys.argv[1]
    else:
        return None

#main driver code
def main():
    macAddress = getMacAddressFromCMD()
    if(macAddress is None):
        print("Please input a MAC address without spaces as command line argument")
    else:
        if(isValidMacAddress(macAddress)):
            print(retrieveNICVendor(macAddress))
        else:
            print("MAC address is not in valid format. Please input a MAC address without spaces as command line argument")


if __name__ == "__main__":
    main()
