
f= open("AuthenticationDetails.txt", "r").read()
print(f)
str=f.split("\n")
dt=str[1]
apik=str[3]
apit=str[5]
ioturl=str[7]
print(dt)
print(apik)
print(apit)
print(ioturl)
#def Convert(str):
    #it = iter(str)
    #res_dct = dict(zip(it, it))
    #return res_dct
#print(Convert(str))


         
    

  