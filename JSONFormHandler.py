import json

databaseDictionary = "orgDatabase.json"
sampleInput = "sampleInput.json"

def getKey(orgDict):
    return orgDict["name"] + " " + orgDict["location"]

def addOrg(form):
    jDict = getDictFromJSON(form)
    database = getDictFromJSON(databaseDictionary)
    try:
        temp = database[getKey(jDict)]
        return False
    except:
        database[getKey(jDict)] = jDict
        with open('orgDatabase.json', 'w') as fp:
            json.dump(database, fp)
        return True

def getOrg(key):
    database = getDictFromJSON(databaseDictionary)
    try:
        return database[getKey(jDict)]
    except:
        return "Org not found!"

def removeOrg(key):
    database = getDictFromJSON(databaseDictionary)
    try:
        org = database[key]
        del database[key]
        with open('orgDatabase.json', 'w') as fp:
            json.dump(database, fp)
        return org
    except:
        return None

def getDictFromJSON(path):
    return json.load(open(path))

if __name__ == '__main__':
    print(addOrg(sampleInput))
    print(removeOrg(getKey(getDictFromJSON(sampleInput))))
