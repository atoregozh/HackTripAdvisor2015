#!/usr/bin/python
# ordering imports
# Standard Library modules
import json

# Third-party library
import requests


def getAttractions(lat, lon, name):
    name.replace (" ", "+")
    url = "http://api.tripadvisor.com/api/partner/2.0/map/" + str(lat) + "," + str(lon) + "," + "/attractions?key=HackTripAdvisor-ade29ff43aed&q=" + name   
    response = requests.get(url)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        location_id = data["data"][0]["location_id"]
        return location_id
    return None


def getReviews(location_id):
    url = "http://api.tripadvisor.com/api/partner/2.0/location/" + location_id + "?key=HackTripAdvisor-ade29ff43aed"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        url = data["reviews"][0]["url"]
        text = data["reviews"][0]["text"]
        return {"review_url":url, "review_text": text}
    return None


def main():
    #TEST Trip
    lat = 40.768924369
    lon = -73.975306691
    nam = "Central Park"

    ids = getAttractions(lat,lon,nam)
    dictn = getReviews(ids)
    print dictn

if __name__ == "__main__":
    main()