import json
from API.NS_API import NS_API

class InfoService(object):
    API = NS_API
    
    def generalTravelInfo():   
        return InfoService.lastDeparturesByStation(station = "UT", limit = 16)[:16]

    def lastDeparturesByStation(station, limit):
        result = InfoService.API.getDepartures(station = station, limit = limit)
        return result['payload']['departures'][:limit]

    def getAllStations():
        result = InfoService.API.getAllStations()
        return result['payload']