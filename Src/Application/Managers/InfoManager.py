import datetime
from API.NS_API import NS_API

class InfoManager(object):
    def getDelay(plannedDateTime, actualDateTime):
        if plannedDateTime == actualDateTime:
            delay = "-"
            return delay
        planned = plannedDateTime.replace('T', ':')
        actual = actualDateTime.replace('T', ':')
        planned = datetime.datetime.strptime(planned[11:16], '%H:%M')
        actual = datetime.datetime.strptime(actual[11:16], '%H:%M')
        delay = actual - planned
        return str(delay)

    def isValidStation(stationName):
        API = NS_API
        stations = API.getAllStations()['payload']

        for station in stations:
            if station["code"] == stationName:
                return station
            elif station["namen"]["lang"] == stationName:
                return station["code"]
            
        return ""

