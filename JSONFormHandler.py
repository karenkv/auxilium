import json

class JSONFormHandler:
    def __init__(self):
        self.databaseDictionary = "orgDatabase.json"
        self.sampleInput = "sampleInput.json"

    def getKeyFromDictionary(self, orgDict):
        return orgDict["name"] + " " + orgDict["location"]

    def getKeyFromJSON(self, path):
        dictionary = self.getDictFromJSON(path)
        return self.getKeyFromDictionary(dictionary)

    def addOrg(self, form):
        jDict = self.getDictFromJSON(form)
        database = self.getDictFromJSON(self.databaseDictionary)
        try:
            temp = database[self.getKeyFromDictionary(jDict)]
            return False
        except:
            database[self.getKeyFromDictionary(jDict)] = jDict
            with open('orgDatabase.json', 'w') as fp:
                json.dump(database, fp)
            return True

    def getOrg(self, key):
        database = self.getDictFromJSON(self.databaseDictionary)
        try:
            return database[key]
        except:
            return "Org not found!"

    def removeOrg(self, key):
        database = self.getDictFromJSON(self.databaseDictionary)
        try:
            org = database[key]
            del database[key]
            with open('orgDatabase.json', 'w') as fp:
                json.dump(database, fp)
                return org
        except:
            return None

    def getDictFromJSON(self, path):
        return json.load(open(path))
