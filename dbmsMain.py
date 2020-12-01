#author: Jigar Makwana B00842568
from queryParser.queryParser import parseQuery
from queryExecutor.queryExecutor import executeQuery
from userManagement import functions
from userManagement import user_class
from execution import Execution

class DBMSMain:
    def DBMSMainMenu(username):
        while( True ):
            print('User in session: ' + username)
            userInput = functions.display_DBMS_options()
            if(userInput == "1"):
                Execution.ExecutionMenu(username)
            elif(userInput == "2"):
                break
            elif(userInput == "3"):
                break
            elif(userInput == "4"):
                break
            elif(userInput == "5"):
                break
            elif(userInput == "6"):
                break
            elif(userInput == "7"):
                isLoggedIn = user_class.User.logOut()
                break
            else:
                print("Please enter a valid option...")
            print("\n")

