#!/usr/bin/python3
"""Alta3 || Tracking ISS"""

import urllib.request
import json

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
        
    ## Call the webservice
    groundctrl = urllib.request.urlopen(MAJORTOM)
    
    ## put fileobject into helmet
    helmet = groundctrl.read()
    
    ## decode JSON to Python data structure
    helmetson = json.loads(helmet.decode('utf-8'))
    
    ## display our Pythonic data
    print("People in space:", helmetson["number"])
    astronaut = helmetson["people"]
    for new in astronaut :
        print(new['name'] + "on the " + new['craft'])
    
   # print('\n\nPeople in Space: ', helmetson['number'])
    #people = helmetson['people']
    #print(people)
    
main()

