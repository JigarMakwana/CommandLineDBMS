dd_path = "dataDictonary/"
import csv
import json

def createMetaData(db_name, parseCreateData):
    jsonData = json.dumps(parseCreateData, indent=4)
    f = open(dd_path + db_name + '.json',"a")
    f.write(jsonData)
    f.close()
    print("\nmetadata file updated!")

def createDBUserMap(dbName, userName):
    mapEntry = [dbName, userName]
    mapData = []
    mapData.append(mapEntry)
    myFile = open(dd_path + 'dbUserMap.csv', 'a', newline='')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(mapData)
    print("\ndbUserMap.csv updated!")