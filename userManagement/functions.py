# author: Jigar Makwana B00842568




def display_options():
    print("\nHello! Welcome to the user CSCI5408 DBMS!")
    userSelction = input("""Please select the option
        1 - Sign In
        2 - Create a new User
        3 - Show Users
        4 - Go To DBMS Menu
        5 - Quit\n""")
    return userSelction


def display_DBMS_options():
    print("\nHello! You are now Logged into CSCI5408 DBMS!")
    userSelction = input("""Please select the option
        1 - Execute Database Queries
        2 - Check General Logs
        3 - Check Event Logs
        4 - Check Data Dictonary
        5 - Create SQL Dump
        6 - Create ERD
        7 - Logout\n""")
    return userSelction


def display_CRUD_options():
    userSelction = input("""Please select the option
        1 - Create a new Database
        2 - Use Existing Database
        3 - Create Table
        4 - Update Table
        5 - Read Table
        6 - Delete Table
        7 - Perform Transaction
        8 - Drop Database
        9 - Go Back\n""")
    return userSelction
