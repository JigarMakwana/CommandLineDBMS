# author: Jigar Makwana B00842568
from queryParser.queryParser import parseQuery
from queryExecutor.queryExecutor import executeQuery, set_db_name
from userManagement import functions
from userManagement import user_class
from os import path, listdir
import csv

db_path = "database/"
dd_path = "dataDictonary/"



class Execution:
    def ExecutionMenu(username):
        while (True):
            print('User in session: ' + username)
            userInput = functions.display_CRUD_options()
            if (userInput == "1"):
                dbname = input("Enter Database Name: ")
                # isDatabaseCreated = executeQuery(dbname + "/")
                if (True):
                    Execution.createDBUserMap(dbname, username)
            elif (userInput == "2"):
                dbname = input("Enter Database Name: ")
                set_db_name(dbname + "/")
            elif (userInput == "3"):
                # createTableQuery = input("Enter Create Table Query: ")
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
                executeQuery()
            elif (userInput == "8"):
                isLoggedIn = user_class.User.logOut()
                break
            else:
                print("Please enter a valid option...")
            print("\n")

    def createDBUserMap(dbName, userName):
        mapEntry = [dbName, userName]
        myFile = open(dd_path + 'dbUserMap.csv', 'a', newline='')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows((mapEntry[0], mapEntry[1]))
        print("\ndbUserMap.csv updated!")
