import json
import csv
from textwrap import indent
from urllib import request
from urllib.error import URLError
import requests
import sys
import pandas as pd
import numpy as np
from tabulate import tabulate
from io import StringIO

#url = "https://gsidemo.messaging.iot.maximoapmsuite-fra04-b3-240f75f72cdf82f997ffe11d34c5adcb-0000.eu-de.containers.appdomain.cloud/api/v0002/application/types/TestPump/devices/TestPump12/events/devicedata"
cafile='/Users/muskanmehrotra/Downloads/gsidemocert.pem'
url = "https://gsidemo.iot.maximoapmsuite-fra04-b3-240f75f72cdf82f997ffe11d34c5adcb-0000.eu-de.containers.appdomain.cloud/api/v0002/device/types/TestPump/mappings"
data = requests.get(url, verify=cafile, auth=("a-gsidemo-pzio1y8ese","AZGYIl_pDrJ-qv15cP"),  headers={'Content-type': 'application/json'})
df = pd.read_csv('rough2.csv')
statauscode=data.status_code
if statauscode==200:
    data0=data.json()
    data1=json.dumps(data0, indent=4, sort_keys=True) #str output,
    data2=json.loads(data1) #list output
    data3=(data2[0]["propertyMappings"]["devicedata"])
    print(data3)
    print(data3.keys())
    filename ="rough2.csv"
    count=int(0)
with open(filename, 'r') as dict1: 
    for line in csv.DictReader(dict1):
        print(line)
        print(len(line))
        if(len(line)==len(data3)):
            print("Column Length Matched")
            len1=len(data3)
            new1=list(data3)
            new2=list(line)
            for i in range(0,len1):
                if(new1[i]==new2[i]):
                    count=count+1
                else:
                    print("Column names in csv header and property names in device type are not matching")
                    print(new1[i])
                    print(new2[i])
            print(count)
    #new_key = list(data3)
    #print(new_key)
#if not(df.columns.equals(data3.keys())) :
    #print("Column Names in CSV Header and Property Names in Device Type are not matching")
#if not(df.columns[0]==new_key[0] and df.columns[1]==new_key[1] and df.columns[2]==new_key[2]  and df.columns[3]==new_key[3]and df.columns[4]==new_key[4] and df.columns[5]==new_key[5]):
     #print("Column Names in CSV Header and Property Names in Device Type are not matching")
#df2 = pd.DataFrame.from_dict(data3, orient ='index')
#print(df2)
if df['dmd'].dtype != np.float64:
    print("Data Type Issue in dmd column")
if df['prs'].dtype != np.float64:
    print("Data Type Issue in prs column")
if df['flow'].dtype != np.float64:
    print("Data Type Issue in flow column")
if df['velocity'].dtype != np.float64:
   print("Data Type Issue in velocity column")
df['EventID'] = df['EventID'].astype("string")
if   (df['EventID'].str.isnumeric().all()):
        print("Data Type issue in Event ID column")
if df['evt_timestamp'].dtype != object:
        print("Data Type issue in evt_timestamp column")
#print(df.dtypes)
#print(type(df['EventID'].str.isnumeric()))
#print(df.to_string())
#for row in range(len(df)):
        #newdict={}
        #for col in df.columns:
            #newdict[col]=df.loc[row,col]
    #print(newdict)
    #jd=json.dumps(newdict,indent=4)
    #print(jd)
        #x=requests.post(url,verify=cafile, auth=(api_key,api_token),json=newdict)
        #print(x)