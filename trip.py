# ordering imports
# Standard Library modules
import json

# Third-party library
import requests

def getattractions(lat, lon, name):
    name.replace (" ", "+")
    url = "http://api.tripadvisor.com/api/partner/2.0/map/" + str(lat) + "," + str(lon) + "," + "/attractions?key=HackTripAdvisor-ade29ff43aed&q=" + str(name)    
    r = requests.get(url)
    print r.text

lat = 40.768924369
lon = -73.975306691
nam = Central Park

getattractions(lat,lon,nam)