""" Import necessary files """
import json
from API.NS_API import NS_API

class InfoService(object):

    """ Instantiate new object based on class. We do this to make it more organised in case we in the future need to create different states of
the object based on constructor inputs """
    API = NS_API

    """ Get general travel info based on station where the NS machine is located from the API,  which for this project is Utrecht Centraal (UT) """
    def generalTravelInfo():   
        return InfoService.lastDeparturesByStation(station = "UT", limit = 16)[:16]

    """ Get last departures by station from the API """
    def lastDeparturesByStation(station, limit):
        result = InfoService.API.getDepartures(station = station, limit = limit)
        return result['payload']['departures'][:limit]

    """ Get all stations from the API """
    def getAllStations():
        result = InfoService.API.getAllStations()
        return result['payload']