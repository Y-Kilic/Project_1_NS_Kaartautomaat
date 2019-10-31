import http.client
import json
import urllib.parse


class NS_API(object):
    
    key = { 'Ocp-Apim-Subscription-Key': '5404c0d6f7b64a6cb3fea06d314058b7' }

    def getDepartures(station, limit):
        try:
            params = urllib.parse.urlencode({'maxJourneys': int(limit), 'station': str(station)})

            conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
            conn.request("GET", "/public-reisinformatie/api/v2/departures?" + params, headers=NS_API.key)

            response = conn.getresponse()
            responsetext = response.read()
            data = json.loads(responsetext)
            
            conn.close()

            return data

        except Exception as e:
            print(e)

    def getAllStations():
        try:
            conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
            conn.request("GET", "/public-reisinformatie/api/v2/stations?", headers=NS_API.key)

            response = conn.getresponse()
            responsetext = response.read()
            data = json.loads(responsetext)
            
            conn.close()

            return data

        except Exception as e:
            print(e)