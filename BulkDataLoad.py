import json
import csv
from textwrap import indent
from urllib import request
from urllib.error import URLError
import time
import requests
import sys
import pandas as pd

device_type=input("Enter the device type: ")
api_key=input("Enter the API Key: ")
api_token=input("Enter the API Token: ")
url = "https://gsidemo.messaging.iot.maximoapmsuite-fra04-b3-240f75f72cdf82f997ffe11d34c5adcb-0000.eu-de.containers.appdomain.cloud/api/v0002/application/types/" + device_type + "/devices/TestPump12/events/devicedata"
cafile='/Users/muskanmehrotra/Downloads/gsidemocert.pem'
y=requests.get(url,verify=cafile)
if(y.status_code!=200):
    print("This device type does not exist, please enter a valid device type")
else:
    if ((api_key=="a-gsidemo-pzio1y8ese") and (api_token=="AZGYIl_pDrJ-qv15cP")) :
        df = pd.read_csv('New.csv')
#print(df.to_string())
        for row in range(len(df)):
            newdict={}
            for col in df.columns:
                newdict[col]=df.loc[row,col]
    #print(newdict)
    #jd=json.dumps(newdict,indent=4)
    #print(jd)
            x=requests.post(url,verify=cafile, auth=(api_key,api_token),json=newdict)
            print(x.status_code)
    elif ((api_key=="a-gsidemo-pzio1y8ese") and (api_token!="AZGYIl_pDrJ-qv15cP")) :
        print("Please enter a valid API Token")
    elif ((api_key!="a-gsidemo-pzio1y8ese") and (api_token=="AZGYIl_pDrJ-qv15cP")) :
        print("Please enter a valid API Key")
    else :
        print("Invalid API Key and API Token")
