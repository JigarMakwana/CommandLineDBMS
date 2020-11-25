from queryParser.queryParser import parseQuery
from queryExecutor.queryExecutor import executeQuery

is_logged_in = True
isin_session = True

if __name__ == '__main__':
    while isin_session:
        username = input("Enter username: ")
        password = input("Enter password: ")
        print("Signing in...")
        # invoke sign in method
        # is_logged_in = sign_in(username, password)
        if is_logged_in:
            dbname = input("Enter database: ")
            executeQuery(dbname + "/")
            isin_session = False
