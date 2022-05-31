import json
from textwrap import indent
from urllib import request
from urllib.error import URLError
from wsgiref import validate
import requests
import sys
import pandas as pd
from tabulate import tabulate

device_type=input("Enter the device type: ")
api_key=input("Enter the API Key: ")
api_token=input("Enter the API Token: ")
url = "https://gsidemo.iot.maximoapmsuite-fra04-b3-240f75f72cdf82f997ffe11d34c5adcb-0000.eu-de.containers.appdomain.cloud/api/v0002/device/types/" + device_type + "/mappings"
if ((api_key=="a-gsidemo-pzio1y8ese") and (api_token=="AZGYIl_pDrJ-qv15cP")) :
  cafile='/Users/muskanmehrotra/Downloads/gsidemocert.pem'
  data = requests.get(url, verify=cafile, auth=(api_key, api_token),  headers={'Content-type': 'application/json'})
  statauscode=data.status_code
  if statauscode==200:
     iotlist_data=data.json()#getting the data in list python list format
     #string_data=json.dumps(iotlist_data, indent=4, sort_keys=True) #giving the string output
     #data2=json.loads(string_data) #converting string output to get a normal python list
     dict_data=(iotlist_data[0])#getting python dictionary from python list
     print(dict_data)
    #final=print(tabulate(data3, headers=['EventID', 'dmd' ,'evt_timestamp' ,'flow' ,'prs' ,'velocity'],tablefmt='orgtbl' ))
  else:
    print("This Device Type does not exists, please enter a valid device type")
elif ((api_key=="a-gsidemo-pzio1y8ese") and (api_token!="AZGYIl_pDrJ-qv15cP")) :
    print("Please enter a valid API Token")
elif ((api_key!="a-gsidemo-pzio1y8ese") and (api_token=="AZGYIl_pDrJ-qv15cP")) :
    print("Please enter a valid API Key")
else :
    print("Invalid API Key and API Token")


