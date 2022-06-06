import json
from textwrap import indent
from urllib import request
from urllib.error import URLError
from wsgiref import validate
import requests
import sys
import pandas as pd
import validators
import sample


device_type=sample.dt
api_key=sample.apik
api_token=sample.apit
iot_url=sample.ioturl
cafile='/Users/muskanmehrotra/Downloads/gsidemocert.pem'

#checking if physical interface is active or not
if ((api_key=="a-gsidemo-pzio1y8ese") and (api_token=="AZGYIl_pDrJ-qv15cP")) :
        piurl = iot_url + "/v0002/device/types/" + device_type + "/physicalinterface"
        pi_data = requests.get(piurl, verify=cafile, auth=(api_key,api_token),  headers={'Content-type': 'application/json'})
        statauscode=pi_data.status_code
        print(statauscode)
        if statauscode==200:
            pi_iotlist_data=pi_data.json()
            print(pi_iotlist_data)
            #print(type(pi_iotlist_data))
            if(pi_iotlist_data["version"]=="active"):
                print("Physical mapping is active")
            else:
                print("Physical mapping is inactive")
        else:
            print("This device type does not exists, enter a valid device type")

        #checking if the logical interface is active or not
        liurl=iot_url + "/v0002/device/types/" + device_type + "/logicalinterfaces"
        li_data = requests.get(liurl, verify=cafile, auth=("a-gsidemo-pzio1y8ese","AZGYIl_pDrJ-qv15cP"),  headers={'Content-type': 'application/json'})
        statauscode=li_data.status_code
        #print(statauscode)
        if statauscode==200:
            li_iotlist_data=li_data.json()
            dict_data=(li_iotlist_data[0])#getting python dictionary from python list
            print(dict_data)
            if(dict_data["version"]=="active"):
                print("Logical mapping is active")
            else:
                print("Logical mapping is inactive")
        #else:
            #print("This device type does not exist, please enter a valid device type")

        #checking physical and logical ampping both are same and active
        if(pi_data.status_code==200) and (li_data.status_code==200):
            if (dict_data["version"]==pi_iotlist_data["version"]):
                print("Physical and Logical mapping matched")
            else:
                print("Physical and logical mapping does not match")
      
elif ((api_key=="a-gsidemo-pzio1y8ese") and (api_token!="AZGYIl_pDrJ-qv15cP")) :
     print("Please enter a valid API Token")
elif ((api_key!="a-gsidemo-pzio1y8ese") and (api_token=="AZGYIl_pDrJ-qv15cP")) :
        print("Please enter a valid API Key")
else :
        print("Invalid API Key and API Token")

