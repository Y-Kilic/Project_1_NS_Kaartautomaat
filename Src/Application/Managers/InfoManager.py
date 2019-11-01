""" Import necessary files """
import datetime
from Services.InfoService import InfoService

class InfoManager(object):

    """ Instantiate new object based on class. We do this to make it more organised in case we in the future need to create different states of
the object based on constructor inputs """
    infoService = InfoService

    """ Checks if there is any delay based on plannedDateTime and actualDateTime, if there is any delay then it returns the delay else a - character """
    def getDelay(plannedDateTime, actualDateTime):
        if plannedDateTime == actualDateTime:
            return "-"

        planned = plannedDateTime.replace('T', ':')
        actual = actualDateTime.replace('T', ':')
        planned = datetime.datetime.strptime(planned[11:16], '%H:%M')
        actual = datetime.datetime.strptime(actual[11:16], '%H:%M')
              
        delay = actual - planned

        return str(delay)[:-3]

    """ Checks based on station code or name if the station exist in the NS API """
    def isValidStation(stationName):
        stations = InfoManager.infoService.getAllStations()

        for station in stations:
            if station["code"].lower() == stationName.lower():
                return station["code"]
            elif station["namen"]["lang"].lower() == stationName.lower():
                return station["code"]
        return ""

    """ Searches for station name based on station code input and if the station exist, returns the long name of the station or if it doesn't exist
   returns an empty string """
    def getStationFullnameByCode(stationCode):
        stations = InfoManager.infoService.getAllStations()

        for station in stations:
            if station["code"].lower() == stationCode.lower():
                return station["namen"]["lang"]
        return ""