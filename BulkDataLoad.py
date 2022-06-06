import json
import csv
from textwrap import indent
from urllib import request
from urllib.error import URLError
import time
import requests
import sys
import pandas as pd
import sample


device_type=sample.dt
api_key=sample.apik
api_token=sample.apit
cafile='/Users/muskanmehrotra/Downloads/gsidemocert.pem'
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
            url = "https://gsidemo.messaging.iot.maximoapmsuite-fra04-b3-240f75f72cdf82f997ffe11d34c5adcb-0000.eu-de.containers.appdomain.cloud/api/v0002/application/types/" + device_type + "/devices/TestPump12/events/devicedata"
            x=requests.post(url,verify=cafile, auth=(api_key,api_token),json=newdict)
            print(x.status_code)
elif ((api_key=="a-gsidemo-pzio1y8ese") and (api_token!="AZGYIl_pDrJ-qv15cP")) :
        print("Please enter a valid API Token")
elif ((api_key!="a-gsidemo-pzio1y8ese") and (api_token=="AZGYIl_pDrJ-qv15cP")) :
        print("Please enter a valid API Key")
else :
        print("Invalid API Key and API Token")
