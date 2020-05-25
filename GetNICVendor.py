#imports
import requests
import sys
import re
import argparse

#calls mac address api to get vendor name and return it
def retrieveNICVendor(macAddress, apiKey):
    #mac address api-endpoint
    API_ENDPOINT = 'https://api.macaddress.io/v1'
    #Output format. To meet requirements, initializing as 'vendor'.
    #Although, can change to 'json' and parse more information from API call
    OUTPUTFORMAT = "vendor"

    ##input parameters for get request:
    PARAMS = {
        'apiKey': apiKey,
        'search': macAddress,
        'output': OUTPUTFORMAT
    }
    #number of seconds to wait for response from web service
    TIMEOUT = 1

    try:
        #try to get a response from GET request
        print("Please wait. Waiting for response")
        #returns a requests.response object
        response = requests.get(API_ENDPOINT, params=PARAMS, timeout = TIMEOUT)
        #raises HTTP exception if we got an error code
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        #check status code and give user appropriate information
        errorMessage = HTTPErrorCodeMessage(response.status_code)
        if(errorMessage is None):
            #user did nothing wrong. exit with message for devs
            raise SystemExit(e)
        else:
            #user did something wrong. Give appropriate Message
            print(errorMessage)
            exit()
    except requests.exceptions.URLRequired:
        print("No URL to API-Endpoint provided")
        raise SystemExit(e)
    except requests.exceptions.InvalidURL:
        print("Invalid URL")
        raise SystemExit(e)
    except requests.exceptions.ConnectionError as e:
        print("Failed to connect to API. Please try again later")
        raise SystemExit(e)
    except requests.exceptions.Timeout:
        #sleep for one second and try again
        print("Connection timed out after "+ TIMEOUT + " seconds. Please wait. Trying again")
        sleep(1)
        try:
            response = requests.get(API_ENDPOINT, params=PARAMS, timeout = TIMEOUT)
        except Exception as e:
            raise SystemExit(e)
    except requests.exceptions.RequestException as e:
        #something really bad has happened
        raise SystemExit(e)

    else:
        return response.text



#translates HTTP Error code into appropriate Error Message
def HTTPErrorCodeMessage(errorCode):
    switcher = {
        401: 'Access restricted. Enter the correct API key',
        402: 'Access restricted. The MacAddress.io account associated with this APIKey has run out of API calls.',
        422: 'Invalid MAC or OUI address was received',
    }
    #either the errorCode is one of the keys in switcher or is not. If not, return NONE
    return switcher.get(errorCode, None)

#determines if passed in string is in valid mac address format
def isValidMacAddress(x):
    #return true if parameter matches regex for mac addresses
    if re.match('([a-fA-F0-9]{2}[:|\-]?){6}$', x):
        return True
    else:
        return False



#main driver code
def main(cmdArgs):
    try:
        macAddress = cmdArgs[1]
        apiKey = cmdArgs[2]
        if((macAddress is None) or (apiKey is None)):
            print("Please input a MAC address withou spaces followed by a space followed by your macaddress.io API key")
        else:
            if(isValidMacAddress(macAddress)):
                print(retrieveNICVendor(macAddress, apiKey))
            else:
                print("MAC address is not in valid format. Please input a MAC address without spaces as command line argument")
    except IndexError as e:
        print("Please input a mac address and APIkey as command line arguments")
        raise e
        print(e)
        exit()
    except (KeyboardInterrupt):
        print('User interrupted program. Exiting')
        exit()


if __name__ == "__main__":
    main(sys.argv)
