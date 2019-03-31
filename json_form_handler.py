import json

class JSONFormHandler:
    def __init__(self):
        self.databaseDictionary = "org_database.json"
        self.sampleInput = "sample_input.json"

    def getKeyFromDictionary(self, orgDict):
        return orgDict["name"] + " " + orgDict["location"]

    def getKeyFromJSON(self, path):
        dictionary = self.getDictFromJSON(path)
        return self.getKeyFromDictionary(dictionary)

    def addOrg(self, path):
        jDict = self.getDictFromJSON(path)
        database = self.getDictFromJSON(self.databaseDictionary)
        try:
            temp = database[self.getKeyFromDictionary(jDict)]
            return False
        except:
            database[self.getKeyFromDictionary(jDict)] = jDict
            with open(self.databaseDictionary, 'w') as fp:
                json.dump(database, fp)
            return True

    def addOrgByDict(self, dict):
        jDict = dict
        database = self.getDictFromJSON(self.databaseDictionary)
        try:
            temp = database[self.getKeyFromDictionary(jDict)]
            return False
        except:
            database[self.getKeyFromDictionary(jDict)] = jDict
            with open(self.databaseDictionary, 'w') as fp:
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
            with open(self.databaseDictionary, 'w') as fp:
                json.dump(database, fp)
                return org
        except:
            return None

    def getDictFromJSON(self, path):
        return json.load(open(path))

    def findByType(self, ty):
        dictionary = self.getDictFromJSON(self.databaseDictionary)
        values = dictionary.values()
        validOrgs = []
        for value in values:
            types = value["types"]
            if ty in types:
                validOrgs.append(value["name"]);
        return validOrgs
