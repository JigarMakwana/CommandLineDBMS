from os import path, listdir
import logging
import time
import queryParser.queryParser as qp

db_path = "database/"
logging.basicConfig(format='%(asctime)s - %(message)s', filename='logs/eventlogs')

db = ''
userName = ''

class transaction:
    def setUserDBName(dbname, username):
        global db, userName
        db = dbname
        userName = username

    def executeQuery():
        db_main = db_path + db
        if path.exists(db_main):
            # database: validation
            print("Into the database: ", db)
            logging.info('User entered valid database: ' + db_main)
            qp.tableNames = listdir(db_path + db)

            # query: validation and parsing
            while True:
                query = input(">> ")
                if(query == "q"):
                    break
                elif(query == "start transaction"):
                    continue
                elif(query == "commit"):
                    commit()
                else:
                    try:
                        parser = qp.parseQuery(query, db, userName)
                        print(parser)

                        # query: select
                        if parser['Type'] == 'select':
                            rows = []
                            with open(db_main + parser['Table'][0].lower()) as table:
                                table_data = table.read().splitlines()
                                table_cols = table_data[0].split(',')

                                if parser['InsertUpdateData'][0] != '*':
                                    indexes = []
                                    for col in parser['InsertUpdateData']:
                                        indexes.append(table_cols.index(col))
                                    for row in table_data:
                                        cols = row.split(',')
                                        row_data = ''
                                        for index in indexes:
                                            row_data += cols[index] + ','
                                        rows.append(row_data[:-1])
                                else:
                                    for row in table_data:
                                        rows.append(row)

                                if len(parser['WhereFields']) == 0:
                                    for element in rows:
                                        print(element)
                                    logging.info('Select query executed successfully.')
                                else:
                                    indexes = [table_cols.index(col) for col in parser['WhereFields']]
                                    conditions_indexes = [0]
                                    for row_idx in range(1, len(table_data)):
                                        table_row = table_data[row_idx].split(',')
                                        for idx in range(len(indexes)):
                                            if table_row[indexes[idx]] == parser['WhereValues'][idx]:
                                                conditions_indexes.append(row_idx)

                                    filtered_rows = []
                                    for idx in range(len(rows)):
                                        if idx in conditions_indexes:
                                            filtered_rows.append(rows[idx])

                                    for element in filtered_rows:
                                        print(element)
                                    logging.info('Select query executed successfully.')

                        # query: insert
                        elif parser['Type'] == 'insert':
                            with open(db_main + parser['Table'][0].lower(), 'a') as table:
                                row = ','.join(col for col in parser['InsertUpdateData'])
                                table.write(row + "\n")
                                print("Successfully inserted the data")

                        # query: update
                        elif parser['Type'] == 'update':
                            print(parser['Table'])                     
                            print(parser['Table'][0])
                            print(parser['Table'][0].lower())
                            isLocked = isLocked(parser['Table'][0].lower())
                            if(isLocked):
                                time.sleep(2)
                                isLocked = isLocked(parser['Table'][0].lower())
                                if(isLocked):
                                    rollback()
                            else:
                                with open(db_main + parser['Table'][0].lower(), 'a') as table:
                                    row = ','.join(col for col in parser['InsertUpdateData'])
                                    table.write(row + "\n")
                                    print("Successfully updated the record in file")

                        # query: delete
                        elif parser['Type'] == 'delete':
                            rows = []
                            table_data_rows = []
                            with open(db_main + parser['Table'][0].lower()) as table:
                                col = parser['WhereFields'][0]
                                table_data_rows = table.readlines()
                                rows.append(table_data_rows[0])
                                header = table_data_rows[0].split(',')
                                for rows_idx in range(1, len(table_data_rows)):
                                    row = table_data_rows[rows_idx]
                                    row_elements = row.split(',')
                                    if row_elements[header.index(col)] != parser['WhereValues'][0]:
                                        rows.append(row)
                            with open(db_main + parser['Table'][0].lower(), 'w') as table:
                                for row in rows:
                                    table.write(row)
                            print("Successfully Deleted the record")

                        # query: create
                        elif parser['Type'] == 'create':
                            with open(db_main + parser['Table'][0].lower(), 'w') as table:
                                print(table)
                            print("Successfully created the table")

                    except:
                        rollback()

        else:
            logging.info('User entered invalid database name.')
            print("Invalid database name")

    def isLocked(tableName):
        myFile = open("dataDictonary/locktracker.csv", 'r')        
        with myFile:
            reader = csv.reader(myFile)
            next(reader, None)
            for row in reader:
                if(row[0] == userName and row[1] == db and row[0] == tableName and row[0] == yes):
                    return False
                elif(row[0] != userName and row[1] == db and row[0] == tableName and row[0] == yes):
                    return True

    def rollback():
        print('\nEither Resource is locked by other user or invalid')
        print('Transaction cannot be completed')

    def commit():
        print('\nCommitting the transaction')