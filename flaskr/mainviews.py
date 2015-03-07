from flask import Flask, render_template, json, url_for, session
import json
from pygeocoder import Geocoder

import useInstaTrip

app = Flask(__name__)

def get_elements(img):
		return [img["latitude"], img["longitude"], img["timestamp"].encode("utf-8"), img["thumbnail"].encode("utf-8")]

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
		images_by_city = {}
		for img in data:
			coordinate = [img["latitude"], img["longitude"]]
			c = city(coordinate)
			if c:
				c_name = c.encode("utf-8")
				locations[c_name] = coordinate
				if c_name not in images_by_city:
					images_by_city[c_name] = []
				images_by_city[c_name].append(get_elements(img))
		#print images_by_city
		return render_template("world_map.html", locations=locations, all_images=images_by_city)

# @app.route('/wall')
# def wall():
# 	data = useInstaTrip.useInsta("mattbg")
# 	data = data[0:5]
# 	print data
# 	return render_template("wall.html")

if __name__ == '__main__':
    app.run(debug=True)
    #app.debug = True
