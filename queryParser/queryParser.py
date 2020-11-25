import re

qType = ""
qTableName = []
qInserts = []
qFields = []
qUpdates = []
qWhereFields = []
qWhereValues = []

reserveWords = ["(", ")", ">=", "<=", "!=", ",", "=", ">", "<", "select", "insert", "values", "update", "delete",
                "where", "from", "set"]
tableNames = ["employee", "department"]
listQuery = []
returnValue = ""


def parseQuery(query):
    oldQuery = query.strip().split(" ")

    for val in oldQuery:
        listQuery.append(val.lower())

    returnValue = False
    qType = listQuery.pop(0)
    if len(listQuery) > 0:
        if qType == "select":
            if checkSelectStep():
                returnValue = True
        elif qType == "insert":
            checkInsertStep()
        elif qType == "update":
            checkUpdateStep()
        elif qType == "delete":
            checkDeleteStep()
    else:
        print("Invalid query")
        returnValue = False

    if returnValue == True:
        parsedData = {
            "Type": qType,
            "Table": qTableName,
            "InsertFields": qInserts,
            "UpdateFields": qUpdates,
            "InsertUpdateData": qFields,
            "WhereFields": qWhereFields,
            "WhereValues": qWhereValues,
            "Error": ""
        }
        return parsedData
    else:
        parsedData = {
            "Error": "Invalid query"
        }
        return parsedData


def checkDeleteStep():
    fromVal = listQuery.pop(0)

    if checkIfFrom(fromVal) and len(listQuery) > 0:
        tableValue = listQuery.pop(0)
        if checkIfTable(tableValue):
            if len(listQuery) > 0:
                whereValue = listQuery.pop(0)
                if whereValue == "where":
                    flag = 0
                    error = 0
                    lastValue = ""
                    list3 = []
                    missing = 0
                    if len(listQuery) != 0:
                        for abc in listQuery:
                            missing = 0
                            if abc != "and":
                                if flag == 0:
                                    list3.append(abc)
                                    if checkIfIdentifier(abc):
                                        qWhereFields.append(abc)
                                        flag = 1
                                        missing = 1
                                    else:
                                        error = 1
                                        break;
                                elif flag == 1:
                                    list3.append(abc)
                                    if checkIfEqualOperator(abc):
                                        flag = 2
                                        missing = 1
                                    else:
                                        error = 2
                                        break;
                                elif flag == 2:
                                    list3.append(abc)
                                    if checkIfStringOrNumber(abc) or checkIfIdentifier(abc):
                                        qWhereValues.append(abc)
                                        flag = 0
                                    else:
                                        lastValue = abc
                                        break;
                            else:
                                missing = 1
                                list3.append(abc)
                        if error == 1:
                            print("Invalid query: identifier expected in where condition")
                            return False
                        elif error == 2:
                            print("Invalid query: operator expected in where condition")
                            return False
                        elif missing == 1:
                            print("Invalid query: expected condition in where clause")
                            return False
                        else:
                            print("Successfully parsed query")
                            return True
                    else:
                        print("Invalid query: condition expected after where clause")
                        return False
                elif len(whereValue) > 0:
                    print("Invalid query")
                    return False
                else:
                    print("Successfully parsed query")
                    return True
            else:
                print("Query Parsed Successfully")
                return True
        else:
            print("Invalid query: Expected keyword FROM and table name")
            return False
    else:
        print("Invalid query: Expected keyword FROM and table name")
        return False


def checkUpdateStep():
    tableVal = listQuery.pop(0)
    if checkIfTable(tableVal):
        setVal = listQuery.pop(0)
        if setVal == "set":
            flag = 0
            error = 0
            lastValue = ""
            list3 = []
            missing = 0
            for abc in listQuery:
                if abc != "where":
                    if abc != ",":
                        missing = 0
                        if flag == 0:
                            list3.append(abc)
                            if checkIfIdentifier(abc):
                                qUpdates.append(abc)
                                flag = 1
                                missing = 1
                            else:
                                error = 1
                                break;
                        elif flag == 1:
                            list3.append(abc)
                            if checkIfEqualOperator(abc):
                                flag = 2
                                missing = 1
                            else:
                                error = 2
                                break;
                        elif flag == 2:
                            list3.append(abc)
                            if checkIfStringOrNumber(abc) or checkIfIdentifier(abc):
                                qFields.append(abc)
                                flag = 0
                            else:
                                lastValue = abc
                                break;
                    else:
                        list3.append(abc)
                        missing = 1
                else:
                    list3.append(abc)
                    lastValue = abc
                    for v in list3:
                        listQuery.remove(v)
                    break;

            if error == 1:
                print("Invalid query: Expected identifier")
                return False
            elif error == 2:
                print('Invalid query: Expected '"="' operator after identifier')
                return False
            elif missing == 1:
                print("Invalid query: expected values to update")
                return False

            if lastValue == "where":
                flag = 0
                error = 0
                lastValue = ""
                list3 = []
                missing = 0
                if len(listQuery) != 0:
                    for abc in listQuery:
                        missing = 0
                        if abc != "and":
                            if flag == 0:
                                list3.append(abc)
                                if checkIfIdentifier(abc):
                                    qWhereFields.append(abc)
                                    flag = 1
                                    missing = 1
                                else:
                                    error = 1
                                    break;
                            elif flag == 1:
                                list3.append(abc)
                                if checkIfEqualOperator(abc):
                                    flag = 2
                                    missing = 1
                                else:
                                    error = 2
                                    break;
                            elif flag == 2:
                                list3.append(abc)
                                if checkIfStringOrNumber(abc) or checkIfIdentifier(abc):
                                    qWhereValues.append(abc)
                                    flag = 0
                                else:
                                    lastValue = abc
                                    break;
                        else:
                            missing = 1
                            list3.append(abc)
                    if error == 1:
                        print("Invalid query: identifier expected in where condition")
                        return False
                    elif error == 2:
                        print("Invalid query: operator expected in where condition")
                        return False
                    elif missing == 1:
                        print("Invalid query: expected condition in where clause")
                        return False
                    else:
                        print("Successfully parsed query")
                        return True
                else:
                    print("Invalid query: condition expected after where clause")
                    return False
            else:
                print("Successfully parsed query")
                return True
        else:
            print("Invalid query: Expected set keyword")
            return False
    else:
        print("Invalid query: Expected table name")
        return False


def checkInsertStep():
    intoVal = listQuery.pop(0)
    if intoVal == "into":
        tableVal = listQuery.pop(0)
        if checkIfTable(tableVal):
            openRoundB = listQuery.pop(0)
            if openRoundB == "(":
                flag = 1
                error = 0
                lastValue = ""
                list3 = []

                for abc in listQuery:
                    if abc != ")":
                        if flag == 1:
                            list3.append(abc)
                            if checkIfIdentifier(abc):
                                flag = 0
                            else:
                                error = 1
                                break;
                        elif flag == 0:
                            list3.append(abc)
                            if checkIfcomma(abc):
                                flag = 1
                            else:
                                lastValue = abc
                                break;
                    elif len(list3) == 0:
                        error = 1
                        break;
                    else:
                        print(list3)
                        list3.append(abc)
                        lastValue = abc
                        for v in list3:
                            if v != "," and v != ")":
                                qInserts.append(v)
                            listQuery.remove(v)
                        break;

                if error == 1:
                    print("Invalid query: expected identifier")
                    return False

                if lastValue == ")":
                    valuesVal = listQuery.pop(0)
                    if valuesVal == "values":
                        openRoundBVal = listQuery.pop(0)
                        if openRoundBVal == "(":
                            flag = 1
                            error = 0
                            lastValue = ""
                            list3 = []
                            for abc in listQuery:
                                if abc != ")":
                                    if flag == 1:
                                        if checkIfStringOrNumber(abc) or checkIfIdentifier(abc):
                                            list3.append(abc)
                                            flag = 0
                                        else:
                                            error = 1
                                            break;
                                    elif flag == 0:
                                        list3.append(abc)
                                        if checkIfcomma(abc):
                                            flag = 1
                                        else:
                                            lastValue = abc
                                            break;
                                elif len(list3) == 0:
                                    error = 1
                                    break;
                                else:
                                    list3.append(abc)
                                    lastValue = abc
                                    for v in list3:
                                        if v != "," and v != ")":
                                            qFields.append(v)
                                        listQuery.remove(v)
                                    break;

                            if error == 1:
                                print("Invalid query: expected values to insert")
                                return False
                            if lastValue == ")":
                                print("Successfully parsed query")
                                return True
                            else:
                                print("Invalid query")
                                return False
                        else:
                            print("Invalid query: Expected round bracket")
                            return False
                    else:
                        print("Invalid query: Expected keyword VALUES")
                        return False
                else:
                    print("Invalid query: Expected round bracket")
                    return False
            else:
                print("Invalid query: Expected round bracket")
                return False
        else:
            print("Invalid query: Expected table name")
            return False
    else:
        print("Invalid insert query: Expected keyword INTO")
        return False


def checkSelectStep():
    x = listQuery.pop(0)

    if checkIfIdentifier(x):
        qFields.append(x)
        y = listQuery.pop(0)
        if checkIfcomma(y):
            checkSelectStep()
        elif checkIfFrom(y):
            z = listQuery.pop(0)
            if not checkIfTable(z):
                print("Invalid table name: " + z)
                return False
        else:
            print("Keyword FROM expected")
            return False
    elif checkIfAsterik(x):
        qFields.append(x)
        y = listQuery.pop(0)
        if checkIfFrom(y):
            z = listQuery.pop(0)
            if not checkIfTable(z):
                print("Invalid table name: " + z)
                return False
        else:
            print("Keyword FROM expected")
            return False
    else:
        print("Invalid query")
        return False

    if len(listQuery) > 0:
        nextValue = listQuery.pop(0)
        if nextValue == "where":
            flag = 0
            error = 0
            lastValue = ""
            list3 = []
            missing = 0
            if len(listQuery) != 0:
                for abc in listQuery:
                    missing = 0
                    if abc != "and":
                        if flag == 0:
                            list3.append(abc)
                            if checkIfIdentifier(abc):
                                qWhereFields.append(abc)
                                flag = 1
                                missing = 1
                            else:
                                error = 1
                                break;
                        elif flag == 1:
                            list3.append(abc)
                            if checkIfEqualOperator(abc):
                                flag = 2
                                missing = 1
                            else:
                                error = 2
                                break;
                        elif flag == 2:
                            list3.append(abc)
                            if checkIfStringOrNumber(abc) or checkIfIdentifier(abc):
                                qWhereValues.append(abc)
                                flag = 0
                            else:
                                lastValue = abc
                                break;
                    else:
                        missing = 1
                        list3.append(abc)
                if error == 1:
                    print("Invalid query: identifier expected in where condition")
                    return False
                elif error == 2:
                    print("Invalid query: operator expected in where condition")
                    return False
                elif missing == 1:
                    print("Invalid query: expected condition in where clause")
                    return False
                else:
                    print("Successfully parsed query")
                    return True
            else:
                print("Invalid query: condition expected after where clause")
                return False
    else:
        print("Successfully parsed query")
        return True


def checkIfIdentifier(identifier):
    pattern = r'^[a-zA-Z_]\w*$'
    if (re.search(pattern, identifier)):
        for word in reserveWords:
            if word == identifier:
                return False
        for table in tableNames:
            if table == identifier:
                return False
        return True
    else:
        return False


def checkIfcomma(comma):
    if comma == ",":
        return True
    else:
        return False


def checkIfEqualOperator(equal):
    if equal == "=":
        return True
    else:
        return False


def checkIfAsterik(asterik):
    if asterik == "*":
        return True
    else:
        return False


def checkIfFrom(fromVal):
    if fromVal == "from":
        return True
    else:
        return False


def checkIfTable(tableVal):
    for tableName in tableNames:
        if tableName == tableVal:
            qTableName.append(tableVal)
            return True
    return False


def checkIfStringOrNumber(value):
    regnumber = re.compile(r'\d+(?:,\d*)?')
    if regnumber.match(value):
        return True
    else:
        return False
