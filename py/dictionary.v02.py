myData = {"effective top tube length": 515, 
        "seat tube length": 500, 
        "seat tube angle": 74.4, 
        "head tube angle": 70.5, 
        "stack": 513, 
        "reach": 367, 
        "standover height": 755} 

for k, v in myData.items():
    print("key:", str(k) + ", value:", str(v))
myKeys = list(myData.keys())
myValues = list(myData.values())

"""
print("Keys:", str(myKeys))
print("Values:", str(myValues))
"""