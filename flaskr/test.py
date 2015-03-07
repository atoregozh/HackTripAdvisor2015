from flask import Flask, render_template, json, url_for
import json
from pygeocoder import Geocoder

app = Flask(__name__)


def city(coordinate):
	place = Geocoder.reverse_geocode(coordinate[0], coordinate[1])
	if not place:
		return None
	else:
		return place[0].city

@app.route('/')
def world_map():
		raw_data = open("igram.json", "r")
		data = json.load(raw_data)
		locations = {}
		for img in data:
			coordinate = [img["location"]["latitude"], img["location"]["longitude"]]
			c = city(coordinate)
			if c:
				locations[c.encode("utf-8").replace(" ", "-")] = coordinate
		print locations
		return render_template("world_map.html", locations=locations)

@app.route('/<city_name>')
def city_map(city_name):
		raw_data = open("igram.json", "r")
		data = json.load(raw_data)
		images = []
		for img in data:
			coordinate = [img["location"]["latitude"], img["location"]["longitude"]]
			c = city(coordinate)
			if c and city_name == c.encode("utf-8").replace(" ", "-"):
				images.append(img)
		return render_template("city_map.html", images=images)

if __name__ == '__main__':
    app.run()
