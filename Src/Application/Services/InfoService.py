import json
from API.NS_API import NS_API
from Managers.ConverterManager import ConverterManager

class InfoService(object):

    def generalTravelInfo():
         converter = ConverterManager
         API = NS_API

         data = API.getDepartures(station = "UT", limit = 25)

         listOfObjects = converter.convertDictToObject(d = data['payload'])

         return listOfObjects