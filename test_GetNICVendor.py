#imports
import GetNICVendor as g
import pytest
import requests
import sys
#testingConfig file is not in repo because it holds apiKey and my macaddress
from testingConfig import apiKeyInputs
from testingConfig import macAddressInputs as macList


def test_retrieveNICVendor():
    assert g.retrieveNICVendor(macList[0], apiKeyInputs[0]) is not None


    with pytest.raises(SystemExit):
        #if mac address cannot be validated by macaddress API, should raise SystemExit
        g.retrieveNICVendor('1233', apiKeyInputs[0])
        #if apikey is invalid, should raise SystemExit
        g.retrieveNICVendor(macList[0], '1233')

@pytest.mark.parametrize('input, result',
                            [
                                (macList[0], True),
                                ('a[h h90 0]', False),
                                ('0000000000000000', False)
                            ]
                        )
def test_isValidMacAddress(input, result):
    assert g.isValidMacAddress(input) is result

@pytest.mark.parametrize('input, result',
                            [
                                (401, 'Access restricted. Enter the correct API key'),
                                (402, 'Access restricted. The MacAddress.io account associated with this APIKey has run out of API calls.'),
                                (422, 'Invalid MAC or OUI address was received'),
                                (None, None),
                                ('something random', None),
                                (34553465, None)
                            ]
                        )
def test_HTTPErrorCodeMessage(input, result):
    assert g.HTTPErrorCodeMessage(input) == result

#test to determine if main catches and IndexError
def test_main():
    with pytest.raises(IndexError):
        g.main([1,2])
