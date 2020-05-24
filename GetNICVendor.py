#imports
import requests
import sys
import re

#calls mac address api to get vendor name and return it
def retrieveNICVendor(macAddress, apiKey):
    #mac address api-endpoint
    API_ENDPOINT = 'https://api.macaddress.io/v1'
    #Output format. To meet requirements, initializing as 'vendor'.
    #Although, can change to 'json' and parse more information from API call
    OUTPUTFORMAT = "vendor"

    ##input parameters for get request:
    #API key from config.py file
    PARAMS = {
        'apiKey': apiKey,
        'search': macAddress,
        'output': OUTPUTFORMAT
    }
    try:
        response = requests.get(API_ENDPOINT, params=PARAMS)
        #raises HTTP exception if we got an error code
        response.raise_for_status()
    except (KeyboardInterrupt, SystemExit):
        print('User interrupted program during GET request. Exiting')
        exit()
    except requests.HTTPError as e:
        #if HTTP error is thrown we can print error message based on HTTP error code
        print(HTTPErrorCodeMessage(response.status_code))
        print(e)
        exit()
    else:
        return response.text

#Python version of Switch-Case thanks to GeeksforGeeks!
def HTTPErrorCodeMessage(errorCode):
    switcher = {
        400: 'Invalid GET Request Parameters',
        401: 'Access restricted. Enter the correct API key',
        402: 'Access restricted. Check the credits balance',
        422: 'Invalid MAC or OUI address was received',
        429: 'Too many requests. Try again later',
        500: 'Internal server error. Try again later or create issue on GitHub'
    }
    return switcher.get(errorCode, 'Unknown Error Code')

#determines if passed in string is in valid mac address format
def isValidMacAddress(x):
    #return true if parameter matches regex for mac addresses
    if re.match('([a-fA-F0-9]{2}[:|\-]?){6}$', x):
        return True
    else:
        return False

#gets the command line argument only if there is one. else returns None
def getMacAddressFromCMD():
    #enforces exactly 2 command line arguments
    if (len(sys.argv) == 3):
        #captures 1st command line argument and returns
        return sys.argv[1]
    else:
        return None

def getApiKey():
    #enforces exactly 2 command line arguments
    if(len(sys.argv) == 3):
        #captures 2nd command line argument and returns
        return sys.argv[2]
    else:
        return None

#main driver code
def main():
    try:
        macAddress = getMacAddressFromCMD()
        apiKey = getApiKey()
        if((macAddress is None) or (apiKey is None)):
            print("Please input a MAC address withou spaces followed by a space followed by your macaddress.io API key")
        else:
            if(isValidMacAddress(macAddress)):
                print(retrieveNICVendor(macAddress, apiKey))
            else:
                print("MAC address is not in valid format. Please input a MAC address without spaces as command line argument")
    except (KeyboardInterrupt, SystemExit):
        print('User interrupted program. Exiting')
        exit()


if __name__ == "__main__":
    main()
