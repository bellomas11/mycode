#!/usr/bin/env python3
import requests
from pprint import pprint as pp # part of the standard library
# import webbrowser

## define some constants
HD = input("Do you want HD")
USER_DATE = input("Enter date of image in YYYY-MM-DD")
NASAAPI = 'https://api.nasa.gov/planetary/apod?' # this is our API to call
MYKEY = 'api_key=GUi3WOIHrksyfld4sz503GhgZlL0l9qymu4sMKTm' ## this is our api key

## pretty print json
def main():
    """run-time code"""
    if len(USER_DATE) >= 1: 
        nasaapiobj = requests.get(NASAAPI + MYKEY+ "&" + USER_DATE) # call the webservice
    else:
        nasaapiobj = requests.get(NASAAPI + MYKEY)
    nasaread = nasaapiobj.json() # parse the JSON blob returned

    # Show converted json
    print(nasaread) # show converted JSON without pprint
    input('\nThis is converted json. Press ENTER to continue.') # pause for enter

    # Show Pretty Print json
    pp(nasaread) # this is pretty print in action
    # pprint.pprint(convertedjson) # if you do a simple import pprint, the result is a long usage
    input('\nThis is pretty printed JSON. Press ENTER to continue.') # pause for ENTER

    # Print the description of the photo we are about to view
    print(nasaread['explanation']) # display the value for the key explanation
    print("Link to the APOD:", nasaread.get('hdurl',"No HD URL for today!"))


    #input('\nPress ENTER to view this photo of the day') # pause for ENTER
    # webbrowser.open(nasaread['hdurl']) # open in the webbrowser

main()

