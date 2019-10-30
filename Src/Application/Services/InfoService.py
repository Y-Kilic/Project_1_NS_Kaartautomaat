import json
from API.NS_API import NS_API

class InfoService(object):

    def generalTravelInfo():
         API = NS_API
         return API.getDepartures(station = "UT", limit = 25)['payload']

    def lastDeparturesByStation(station, limit):
         API = NS_API
         return API.getDepartures(station = station, limit = limit)['payload']['departures']