from flask import Flask, render_template, json, url_for, request
import json
from pygeocoder import Geocoder
import useInstaTrip
from urllib2 import urlopen
import time
import requests
from geopy.geocoders import Nominatim
app = Flask(__name__)

def get_elements(img):
		return [img["latitude"], img["longitude"], img["timestamp"].encode("utf-8"), img["thumbnail"].encode("utf-8")]

def getCity(coordinate):
    url = "http://api.tripadvisor.com/api/partner/2.0/map/" + str(coordinate[0]) + "," + str(coordinate[1]) + "," + "/geos?key=HackTripAdvisor-ade29ff43aed"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        city = data["data"][0]["name"]
        return city
    return None

def city(coordinate):
	place = Geocoder.reverse_geocode(coordinate[0], coordinate[1])
	if not place:
		return None
	else:
		return place[0].city

@app.route('/')
def login():
	return render_template("login.html")
	

@app.route('/world_map', methods=['GET'])
def world_map():
		username = request.args.get("igid")
		data = useInstaTrip.useInsta(username)
		locations = {}
		images_by_city = {}
		for img in data:
			if "latitude" not in img or "longitude" not in img:
				continue
			coordinate = [img["latitude"], img["longitude"]]
			#c = "boston" #city(coordinate)
			c = getCity(coordinate)
			if c:
				c_name = c.encode("utf-8")
				locations[c_name] = coordinate
				if c_name not in images_by_city:
					images_by_city[c_name] = []
				images_by_city[c_name].append(get_elements(img))
		print images_by_city
		return render_template("world_map.html", locations=locations, all_images=images_by_city)

if __name__ == '__main__':
		app.debug = True
		app.run()
