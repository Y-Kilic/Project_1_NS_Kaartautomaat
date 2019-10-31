from Services.InfoService import InfoService


infoService = InfoService
departures = infoService.generalTravelInfo()

for departure in departures:
    ## laat zien welke attributes in per departure zit.
    print("###########################################################")
    print(departure.keys())
    print("###########################################################")

    ## dus je kan nu variables gebruiken om te krijgen wat je wilt bv
    print(f"Departure naam is: {departure['name']}")
    print(f"Departure tijd is: {departure['plannedDateTime']}")