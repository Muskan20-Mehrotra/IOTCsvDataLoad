# IOTCsvDataLoad
Step 1 : The user/developer needs to add the authetication details in "authetication.txt" file , this will reduce the time and efforts required from the developer as now they need to enter the details only once and those same details will be processed or taken as input automatically to complete the rest of the actions.
Step 2 : The python code will import this text file and will convert it into a python format text.
Ste 3 : The "Get Method.py will now establish a connection with the IOT Platform and get all the property mappings of the mentioned device type.
Step 4: Then we move to bulk data load so we will use "Bulk Data Load.py" where we uploaded the csv file and processeded it to send the bulk data to our IOT platform.
Step 4 : Now for the validation of the bulk data we use "Validation.py" to validate the csv file data and then tried to get the csv data validated before sending it to IOT Platform
Step 5 : Its very important to match the physical and logical interface for the mentioned device sp For matching Physical and logical mapping we tried to match th interfaces and validate the parameters in "PiandLi.py".
<img width="1792" alt="Screenshot 2022-05-31 at 1 14 47 PM" src="https://user-images.githubusercontent.com/64595118/171120087-1d806bc7-cf7d-434e-b8c4-24d1918fa59e.png">
