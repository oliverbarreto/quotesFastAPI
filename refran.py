import json, random

class Refran:

    @classmethod
    def getRandomRefran(cls):
        data = Refran.getRefranes()
        return data["refranes"][random.randint(0,len(data["refranes"])-1)]

    @classmethod
    def getRandomSaying(cls):
        data = Refran.getRefranes()
        return data["sayings"][random.randint(0,len(data["sayings"])-1)]

    @classmethod
    def getRefranes(cls):
        return json.load(open("data.json"))
    