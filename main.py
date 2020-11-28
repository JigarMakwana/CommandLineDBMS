#author: Jigar Makwana B00842568
import sys
from userManagement.user_class import User
from userManagement.functions import display_options
from dbmsMain import DBMSMain

User.loadDatabase()
# user_class.User.generateKey() Needs to be run only once

isLoggedIn = False

if __name__ == '__main__':
    while( True ):
        userInput = display_options()
        if(userInput == "1"):
            username = input("Please enter a Username: ") 
            password = input("Please enter a Password: ")
            isLoggedIn = User.signIn(username, password)
            if(isLoggedIn):
                print("\nSuccessfully Signed into CSCI5408 DBMS")
                DBMSMain.DBMSMainMenu()
            else:
                print("\nPlease try again..")
        elif(userInput == "2"):
            username = input("Please enter a Username: ") 
            password = input("Please enter a Password: ")
            User.addUser(username, password)
        elif(userInput == "3"):
            User.displayUsers()
        elif(userInput == "5"):   
            print("Quitting CSCI5408 DBMS....")
            sys.exit(0)
        else:
            print("Please enter a valid option...")
        print("\n")