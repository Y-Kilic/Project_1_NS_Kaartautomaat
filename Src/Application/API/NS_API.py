import http.client
import json
import urllib.parse

key = { 'Ocp-Apim-Subscription-Key': '5404c0d6f7b64a6cb3fea06d314058b7' }

class NS_API(object):
    def __init__(self):
        global key
        return

    def getDepartures(station, limit):
        try:
            params = urllib.parse.urlencode({'maxJourneys': int(limit), 'station': str(station)})

            conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
            conn.request("GET", "/public-reisinformatie/api/v2/departures?" + params, headers=key)

            response = conn.getresponse()
            responsetext = response.read()
            data = json.loads(responsetext)
            
            conn.close()

            return data

        except Exception as e:
            print(e)