# Get NIC Vendor Name
Description:
This program is a Python Script that accepts a MAC address as command line argument and returns the name of the vendor of the Network Interface Controller associated with the MAC address. Internally, the script calls the macaddress.io API via a GET request to obtain information related to the MAC address.

HOW TO USE:
1. Get an API Key from macaddress.io by registering for an account on the website
2. Run GetNICVendor.py followed by a MAC address without spaces followed by your API Key from step 1

Security Concerns:
My API key and MAC address are publically exposed in this repository and could be stored in server logs when using GET. The API key could be used to perform a DOS attack on the macaddress.io servers. Hopefully, the server has implemented some kind of spike arrest to prevent this. A MAC address is potentially sensitive as well.

Built on Python 3.8.2
