import json

database = 'sessions_database.json'

def createSession(pNumber):
    dictionary = getDatabase()
    try:
        value = dictionary[pNumber]
        return False
    except:
        session = {}
        session["state"] = 0
        session["ip"] = ""
        session["desire"] = ""

        dictionary[pNumber] = session
        with open(database, 'w') as fp:
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
    with open(database, 'w') as fp:
        json.dump(dictionary, fp)

def setIP(pNumber, ip):
    dictionary = getDatabase()
    session = dictionary[pNumber]
    session["ip"] = ip
    with open(database, 'w') as fp:
        json.dump(dictionary, fp)

def setDesire(pNumber, desire):
    dictionary = getDatabase()
    session = dictionary[pNumber]
    session["desire"] = desire
    with open(database, 'w') as fp:
        json.dump(dictionary, fp)

def deleteSession(pNumber):
    dictionary = getDatabase()
    del dictionary[pNumber]
    with open(database, 'w') as fp:
        json.dump(dictionary, fp)

def getSession(pNumber):
    dictionary = getDatabase()
    try:
        return dictionary[pNumber]
    except:
        return None

def getDatabase():
    return json.load(open(database))
