#author: Jigar Makwana B00842568
import csv

parseData = {
  "Database": 'jigardb',
  "UserName": 'jigar',
  "Table": 'Orders',
  "Cloumn": [    {
    "Name": "OrderID",
    "DataType": "varchar(255)",
    "isUnique": "True",
    "isNotNull": "True",
    "isAutoIncrement": "True",
    "isPrimaryKey": "True",
    "isForeignKey": "False",
    "references": "",
    "default": ""
    },
    {
    "Name": "PersonID",
    "DataType": "varchar(255)",
    "isUnique": "False",
    "isNotNull": "False",
    "isAutoIncrement": "False",
    "isPrimaryKey": "False",
    "isForeignKey": "True",
    "references": "Persons(PersonID)",
    "default": "Hello"
    }]  
}

def generateERD():
    print(parseData)
    print('\nTable Name is :' + parseData["Database"])
    print('Column details are as follow: \n')
    for index in range(len(parseData["Cloumn"])):
        for key in parseData["Cloumn"][index]:
            if(key == "Name"):
                print('Column Name is :' + parseData["Cloumn"][index]["Name"])
            elif(key == "DataType"):
                print('Column Data Type is :' + parseData["Cloumn"][index]["DataType"])
            elif(key == "isUnique"):
                if(parseData["Cloumn"][index]["isUnique"] == "True"):
                    print(parseData["Cloumn"][index]["Name"] + ' is Unique')
                else:
                    print(parseData["Cloumn"][index]["Name"] + ' is not Unique')
            elif(key == "isNotNull"):
                if(parseData["Cloumn"][index]["isNotNull"] == "True"):
                    print(parseData["Cloumn"][index]["Name"] + ' cannot be Not Null')
                else:
                    print(parseData["Cloumn"][index]["Name"] + ' can be Null')
            elif(key == "isAutoIncrement"):
                if(parseData["Cloumn"][index]["isAutoIncrement"] == "True"):
                    print(parseData["Cloumn"][index]["Name"] + ' is Auto Increment')
                else:
                    print(parseData["Cloumn"][index]["Name"] + ' is not Auto Increment')
            elif(key == "isPrimaryKey"):
                if(parseData["Cloumn"][index]["isPrimaryKey"] == "True"):
                    print(parseData["Cloumn"][index]["Name"] + ' is PrimaryKey')
                else:
                    print(parseData["Cloumn"][index]["Name"] + ' is not PrimaryKey')
            elif(key == "isForeignKey"):
                if(parseData["Cloumn"][index]["isForeignKey"] == "True"):
                    print(parseData["Cloumn"][index]["Name"] + ' is ForeignKey')
                else:
                    print(parseData["Cloumn"][index]["Name"] + ' is not ForeignKey')
            elif(key == "references"):
                if(parseData["Cloumn"][index]["references"] != ""):
                    print(parseData["Cloumn"][index]["Name"] + ' references ' + parseData["Cloumn"][index]["references"])
            elif(key == "default"):
                if(parseData["Cloumn"][index]["default"] != ""):
                    print(parseData["Cloumn"][index]["Name"] + "'s default value is " + parseData["Cloumn"][index]["default"])
                    print("\n")
                else:
                    print(parseData["Cloumn"][index]["Name"] + ' does not have any default value')
                    print("\n")