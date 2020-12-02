# author: Jigar Makwana B00842568
from queryParser.queryParser import parseQuery
# from queryExecutor.queryExecutor import executeQuery, set_db_name
from queryExecutor.transactionMngr import executeQuery, setUserDBName
from userManagement import functions
from userManagement import user_class
from os import path, listdir
import csv
import json

db_path = "database/"
dd_path = "dataDictonary/dbDic/"
db_name = ''

class Execution:
    def set_db_name(dbname):
        global db_name
        db_name = dbname
        
    def ExecutionMenu(username):
        while (True):
            print('User in session: ' + username)
            userInput = functions.display_CRUD_options()
            if (userInput == "1"):
                dbname = input("Enter a new Database Name: ")
                # isDatabaseCreated = executeQuery(dbname + "/")
                if (True):
                    Execution.createDBUserMap(dbname, username)
            elif (userInput == "2"):
                dbname = input("Enter an existing Database Name: ")
                Execution.set_db_name(dbname)
                setUserDBName(dbname + "/" , username)
                print(dbname + ' database selected successfully')
            elif (userInput == "3"):
                dbname = input("Enter a new Database Name: ")
                Execution.set_db_name(dbname)
                createTableQuery = input("Enter Create Table Query: ")
                Execution.createMetaData(db_name, parseQuery(createTableQuery, db_name, username))
                executeQuery()
            elif (userInput == "4"):
                # updateTableQuery = input("Enter Update Table Query: ")
                executeQuery()
            elif (userInput == "5"):
                # readTableQuery = input("Enter Read Table Query: ")
                executeQuery()
            elif (userInput == "6"):
                # deleteTableQuery = input("Enter Delete Table Query: ")
                executeQuery()
            elif (userInput == "7"):
                # deleteTableQuery = input("Enter Database Name to drop: ")
                transactionManger()
            elif (userInput == "8"):
                # deleteTableQuery = input("Enter Database Name to drop: ")
                executeQuery()
            elif (userInput == "9"):
                isLoggedIn = user_class.User.logOut()
                break
            else:
                print("Please enter a valid option...")
            print("\n")

    def createDBUserMap(dbName, userName):
        mapEntry = [dbName, userName]
        mapData = []
        mapData.append(mapEntry)
        myFile = open(dd_path + 'dbUserMap.csv', 'a', newline='')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(mapData)
        print("\ndbUserMap.csv updated!")

    def createMetaData(db_name, parseCreateData):
        jsonData = json.dumps(parseCreateData, indent=4)
        f = open(dd_path + db_name + '.json',"a")
        f.write(jsonData)
        f.close()
        print("\nmetadata file updated!")

