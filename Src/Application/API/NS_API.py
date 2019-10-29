import http.client
import json
import urllib.parse

class NS_API(object):
    """description of class"""

    key = "5404c0d6f7b64a6cb3fea06d314058b7"

    def generalTravelInfo(station):
        params = urllib.parse.urlencode({
        'maxJourneys': '25',
        'station': str(station)
        })

        try:
            conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
            conn.request("GET", "/public-reisinformatie/api/v2/departures?" + params, headers=key)

            response = conn.getresponse()
            responsetext = response.read()
            data = json.loads(responsetext)
   
            return data
            conn.close()

        except Exception as e:
            print("Fout: {} {}".format(e.errno, e.strerror))