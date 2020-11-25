from os import path, listdir
import queryParser.queryParser as qp

db_path = "database/"


def executeQuery(dbname):
    db = db_path + dbname
    if path.exists(db):

        # database: validation
        print("Into the database: ", dbname)
        qp.tableNames = listdir(db_path + dbname)

        # query: validation and parsing
        while True:
            query = input(">> ")
            try:
                parser = qp.parseQuery(query)

                # query: execution
                with open(db + parser['Table'][0].lower()) as table:
                    print(table.read())
            except:
                print("Operation failed, try again..")

    else:
        print("Invalid database name")
