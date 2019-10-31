from Services.InfoService import InfoService
from Managers.InfoManager import InfoManager
from tkinter import *
from tkinter import messagebox
import datetime

infoService = InfoService
infoManager = InfoManager
# GUI list of departures
def show_departures(stationCode):
    GUImenu.pack_forget()
    GUIdepartures.pack()
    
    departures = infoService.lastDeparturesByStation(station = stationCode, limit = 16)
    stationName = infoManager.getStationFullnameByCode(stationCode)

    root.title("Actuele reisinformatie voor: " + str(stationName))
    Label(master=GUIdepartures, text=("Actuele reisinformatie voor: " + str(stationName)), font=buttonFont, foreground=nsBlue, background=nsYellow).place(x=300, y=20)
    Button(master=GUIdepartures, text="< Terug naar menu", font=buttonFont, foreground=nsWhite, background=nsBlue, command=main_menu).place(x=10, y=10)

    Label(master=GUIdepartures, text="Geplande \nvertrektijd", font=buttonFont, foreground=nsBlueDark, background=nsYellow).place(x=120, y=47)
    Label(master=GUIdepartures, text='Richting', font=buttonFont, foreground=nsBlueDark, background=nsYellow).place(x=230, y=65)
    Label(master=GUIdepartures, text='Spoor', font=buttonFont, foreground=nsBlueDark, background=nsYellow).place(x=360, y=65)
    Label(master=GUIdepartures, text='Type', font=buttonFont, foreground=nsBlueDark, background=nsYellow).place(x=430, y=65)
    Label(master=GUIdepartures, text='Vertraging', font=buttonFont, foreground=nsBlueDark, background=nsYellow).place(x=520, y=65)
    Label(master=GUIdepartures, text='Verwachte \nvertrektijd', font=buttonFont, foreground=nsBlueDark, background=nsYellow).place(x=660, y=47)

    yaxis = 100
    for departure in departures:
        Label(master=GUIdepartures, text=departure['plannedDateTime'][11:16], font=credFont, foreground=nsBlueDark, background=nsYellow).place(x=160, y=yaxis)
        Label(master=GUIdepartures, text=departure['direction'], font=credFont, foreground=nsBlueDark, background=nsYellow).place(x=230, y=yaxis)
        Label(master=GUIdepartures, text=departure['plannedTrack'], font=credFont, foreground=nsBlueDark, background=nsYellow).place(x=375, y=yaxis)
        Label(master=GUIdepartures, text=departure['trainCategory'], font=credFont, foreground=nsBlueDark, background=nsYellow).place(x=445, y=yaxis)
        Label(master=GUIdepartures, text=InfoManager.getDelay(departure['plannedDateTime'], departure['actualDateTime']), font=credFont, foreground=nsBlueDark, background=nsYellow).place(x=525, y=yaxis)
        Label(master=GUIdepartures, text=departure['actualDateTime'][11:16], font=credFont, foreground=nsBlueDark, background=nsYellow).place(x=670, y=yaxis)
        yaxis += 25

# GUI station validator
def station_validator(selectedStation):
    stationCode = infoManager.isValidStation(selectedStation)
    if (len(stationCode) < 1):
        messagebox.showinfo("Foutmelding", "Geen station gevonden, probeert u het alstublieft opnieuw.")
    else:
        show_departures(stationCode)

# GUI unavailable functions pop-up
def out_of_order():
    messagebox.showinfo("Foutmelding", "Deze functie is tijdelijk niet beschikbaar. Excuses voor het ongemak!")

# GUI station selection
def select_station():
    searchBar.place(x=600, y=390)
    Label(master=GUImenu, text="Van welk station \nwilt u de vertrekinformatie?", font=buttonFont, foreground=nsBlueDark, background=nsYellow).place(x=555, y=340)
    Label(master=GUImenu, text="bijv. 'Utrecht Centraal'", font=credFont, foreground=nsBlueDark, background=nsYellow).place(x=600, y=420)
    Button(master=GUImenu, text="Zoek", font=credFont, foreground=nsWhite, background=nsBlue, command=lambda: station_validator(searchBar.get())).place(x=730, y=386)

# GUI main menu function
def main_menu():
    for widget in GUIdepartures.winfo_children():
        widget.destroy()
    GUIdepartures.pack_forget()
    GUImenu.pack()
    root.title("NS Kaartautomaat")

# GUI fonts & colours
splashFont = ("Helvetica", 48, "bold")
buttonFont = ("Helvetica", 12, "bold")
credFont = ("Helvetica", 10)

nsBlue = "#0000A5"      # Buttons
nsBlueDark = "#002C8C"  # Splash text
nsYellow = "#FFC800"    # Background
nsWhite = "#FFFFFF"     # Button text
nsRed = "FF0000"        # Used in nsDelay

# GUI setup
root = Tk()

# GUI main menu frame
GUImenu = Frame(master=root)
GUImenu.configure(height=700, width=940, background=nsYellow)

Label(master=GUImenu, text="Welkom bij NS", font=splashFont, foreground=nsBlueDark, background=nsYellow).place(x=250, y=100)
Label(master=GUImenu, text="By: Annastazia, Thijs, Yaser & Yasin", font=credFont, foreground=nsBlueDark, background=nsYellow).place(x=700, y=670)

buttonAmsterdam = Button(master=GUImenu, text="Ik wil naar \nAmsterdam", foreground=nsWhite, background=nsBlue, font=buttonFont, command=out_of_order, height=3, width=15).place(x=120, y=250)
buttonKaartje = Button(master=GUImenu, text="Kopen \nlos kaartje", foreground=nsWhite, background=nsBlue, font=buttonFont, command=out_of_order, height=3, width=15).place(x=300, y=340)
buttonOV = Button(master=GUImenu, text="Kopen \n OV-chipkaart", foreground=nsWhite, background=nsBlue, font=buttonFont, command=out_of_order, height=3, width=15).place(x=120, y=340)
buttonBuitenland = Button(master=GUImenu, text="Ik wil naar \nhet buitenland", foreground=nsWhite, background=nsBlue, font=buttonFont, command=out_of_order, height=3, width=15).place(x=300, y=250)
buttonDepartures = Button(master=GUImenu, text="Opzoeken \n vertrektijden", foreground=nsWhite, background=nsBlue, font=buttonFont, command=select_station, height=3, width=33).place(x=120, y=450)

searchBar = Entry(master=GUImenu)

# GUI departures frame
GUIdepartures = Frame(master=root)
GUIdepartures.configure(height=700, width=940, background=nsYellow)




main_menu()
root.mainloop()

#for departure in result['departures']:
#    ## laat zien welke attributes in per departure zit.
#    print("###########################################################")
#    print(departure.keys())
#    print("###########################################################")
#    ## dus je kan nu variables gebruiken om te krijgen wat je wilt bv
#    print(f"Departure naam is: {departure['name']}")
#    print(f"Departure tijd is: {departure['plannedDateTime']}")