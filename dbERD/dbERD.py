#author: Jigar Makwana B00842568
import csv
import json

def generateERD(dbname):
    filepath = 'dataDictonary/' + dbname +'.json'
    with open(filepath) as json_file:
        parseData = json.load(json_file)
    erdList = []
    print('\nPrinting ERD...')
    print('\nTable Name is :' + parseData["Database"])
    erdList.append('\nTable Name is :' + parseData["Database"])
    erdList.append('Column details are as follow: \n')
    print('Column details are as follow: \n')
    for index in range(len(parseData["Cloumn"])):
        for key in parseData["Cloumn"][index]:
            if(key == "Name"):
                print('Column Name is :' + parseData["Cloumn"][index]["Name"])
                erdList.append('Column Name is :' + parseData["Cloumn"][index]["Name"])
            elif(key == "DataType"):
                print('Column Data Type is :' + parseData["Cloumn"][index]["DataType"])
                erdList.append('Column Data Type is :' + parseData["Cloumn"][index]["DataType"])
            elif(key == "isUnique"):
                if(parseData["Cloumn"][index]["isUnique"] == "True"):
                    print(parseData["Cloumn"][index]["Name"] + ' is Unique')
                    erdList.append(parseData["Cloumn"][index]["Name"] + ' is Unique')
                else:
                    print(parseData["Cloumn"][index]["Name"] + ' is not Unique')
                    erdList.append(parseData["Cloumn"][index]["Name"] + ' is not Unique')
            elif(key == "isNotNull"):
                if(parseData["Cloumn"][index]["isNotNull"] == "True"):
                    print(parseData["Cloumn"][index]["Name"] + ' cannot be Not Null')
                    erdList.append(parseData["Cloumn"][index]["Name"] + ' cannot be Not Null')
                else:
                    print(parseData["Cloumn"][index]["Name"] + ' can be Null')
                    erdList.append(parseData["Cloumn"][index]["Name"] + ' cannot be Null')
            elif(key == "isAutoIncrement"):
                if(parseData["Cloumn"][index]["isAutoIncrement"] == "True"):
                    print(parseData["Cloumn"][index]["Name"] + ' is Auto Increment')
                    erdList.append(parseData["Cloumn"][index]["Name"] + ' is Auto Increment')
                else:
                    print(parseData["Cloumn"][index]["Name"] + ' is not Auto Increment')
                    erdList.append(parseData["Cloumn"][index]["Name"] + ' is not Auto Increment')
            elif(key == "isPrimaryKey"):
                if(parseData["Cloumn"][index]["isPrimaryKey"] == "True"):
                    print(parseData["Cloumn"][index]["Name"] + ' is PrimaryKey')
                    erdList.append(parseData["Cloumn"][index]["Name"] + ' is PrimaryKey')
                else:
                    print(parseData["Cloumn"][index]["Name"] + ' is not PrimaryKey')
                    erdList.append(parseData["Cloumn"][index]["Name"] + ' is not PrimaryKey')
            elif(key == "isForeignKey"):
                if(parseData["Cloumn"][index]["isForeignKey"] == "True"):
                    print(parseData["Cloumn"][index]["Name"] + ' is ForeignKey')
                    erdList.append(parseData["Cloumn"][index]["Name"] + ' is ForeignKey')
                else:
                    print(parseData["Cloumn"][index]["Name"] + ' is not ForeignKey')
                    erdList.append(parseData["Cloumn"][index]["Name"] + ' is not ForeignKey')
            elif(key == "references"):
                if(parseData["Cloumn"][index]["references"] != ""):
                    print(parseData["Cloumn"][index]["Name"] + ' references ' + parseData["Cloumn"][index]["references"])
                    erdList.append(parseData["Cloumn"][index]["Name"] + ' references ' + parseData["Cloumn"][index]["references"])
            elif(key == "default"):
                if(parseData["Cloumn"][index]["default"] != ""):
                    print(parseData["Cloumn"][index]["Name"] + "'s default value is " + parseData["Cloumn"][index]["default"])
                    erdList.append(parseData["Cloumn"][index]["Name"] + "'s default value is " + parseData["Cloumn"][index]["default"])
                    print("\n")
                    erdList.append("\n")
                else:
                    print(parseData["Cloumn"][index]["Name"] + ' does not have any default value')
                    erdList.append(parseData["Cloumn"][index]["Name"] + ' does not have any default value')
                    print("\n")
                    erdList.append("\n")

    filepath = 'dbERD/' + dbname + 'ERD.txt'
    MyFile=open(filepath,'w')
    for element in erdList:
        MyFile.write(element)
        MyFile.write('\n')
    MyFile.close()
    print('\nERD sucessfully dumped in file!')
