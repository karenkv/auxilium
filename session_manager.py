import json

database = 'sessions_database.json'

def createSession(pNumber):
    dictionary = getDatabase()
    try:
        value = dictionary[pNumber]
        return False
    except:
        session = {}
        session["State"] = 0
        session["ip"] = ""
        session["desire"] = ""

        dictionary[pNumber] = session
        with open('sessions_database.json', 'w') as fp:
            json.dump(dictionary, fp)
        return True

def findSession(pNumber):
    dictionary = getDatabase()
    try:
        return dictionary[pNumber]
    except:
        return None

def setState(pNumber, state):
    dictionary = getDatabase()
    session = dictionary[pNumber]
    session["state"] = state
    with open('sessions_database.json', 'w') as fp:
        json.dump(dictionary, fp)

def setIP(pNumber, ip):
    dictionary = getDatabase()
    session = dictionary[pNumber]
    session["ip"] = ip
    with open('sessions_database.json', 'w') as fp:
        json.dump(dictionary, fp)

def setDesire(pNumber, desire):
    dictionary = getDatabase()
    session = dictionary[pNumber]
    session["desire"] = desire
    with open('sessions_database.json', 'w') as fp:
        json.dump(dictionary, fp)

def deleteSession(pNumber):
    dictionary = getDatabase()
    del dictionary[pNumber]
    with open('orgDatabase.json', 'w') as fp:
        json.dump(database, fp)

def getDatabase():
    return json.load(open(database))
