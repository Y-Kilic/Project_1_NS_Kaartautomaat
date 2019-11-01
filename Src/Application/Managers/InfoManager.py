import datetime
from Services.InfoService import InfoService

class InfoManager(object):
    infoService = InfoService

    def getDelay(plannedDateTime, actualDateTime):
        if plannedDateTime == actualDateTime:
            return "-"

        planned = plannedDateTime.replace('T', ':')
        actual = actualDateTime.replace('T', ':')
        planned = datetime.datetime.strptime(planned[11:16], '%H:%M')
        actual = datetime.datetime.strptime(actual[11:16], '%H:%M')
              
        delay = actual - planned

        return delay[:-3]

    def isValidStation(stationName):
        stations = InfoManager.infoService.getAllStations()

        for station in stations:
            if station["code"].lower() == stationName.lower():
                return station["code"]
            elif station["namen"]["lang"].lower() == stationName.lower():
                return station["code"]
        return ""

    def getStationFullnameByCode(stationCode):
        stations = InfoManager.infoService.getAllStations()

        for station in stations:
            if station["code"].lower() == stationCode.lower():
                return station["namen"]["lang"]
        return ""

