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

        try:
            delay = str(actual - planned)
        except:
            delay = "-"
            print(f"Er is iets fout gegaan met {delay}")

        return delay[:-3]

    def isValidStation(stationName):
        API = NS_API
        stations = API.getAllStations()['payload']

        for station in stations:
            if station["code"].lower() == stationName.lower():
                return station["code"]
            elif station["namen"]["lang"].lower() == stationName.lower():
                return station["code"]
            
        return ""
    def getStationFullnameByCode(stationCode):
        API = NS_API
        stations = API.getAllStations()['payload']

        for station in stations:
            if station["code"].lower() == stationCode.lower():
                return station["namen"]["lang"]
        return ""

