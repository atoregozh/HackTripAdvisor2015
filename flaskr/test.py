from flask import Flask, render_template, url_for, request
import json
import useInstaTrip
from urllib2 import urlopen
import time
import requests
app = Flask(__name__)

N = 20

def get_elements(img):
		return [img["latitude"], img["longitude"], img["thumbnail"].encode("utf-8")]

def getState(coordinate):
    url = "http://api.tripadvisor.com/api/partner/2.0/map/" + str(coordinate[0]) + "," + str(coordinate[1]) + "," + "/geos?key=HackTripAdvisor-ade29ff43aed"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        state = data["data"][0]["address_obj"]["state"]
        return state
    return None


@app.route('/')
def login():
	return render_template("login.html")
	

@app.route('/world_map', methods=['GET'])
def world_map():
		username = request.args.get("igid")
		data = useInstaTrip.useInsta(username)[1:N]
		locations = {}
		images_by_city = {}
		center = [0.0, 0.0]
		count = 0
		for img in data:
			if "latitude" not in img or "longitude" not in img:
				continue
			coordinate = [img["latitude"], img["longitude"]]
			c = getState(coordinate)
			if c:
				c_name = c.encode("utf-8")
				locations[c_name] = coordinate
				if c_name not in images_by_city:
					images_by_city[c_name] = []
				images_by_city[c_name].append(get_elements(img))
				center[0] += coordinate[0]
				center[1] += coordinate[1]
				count += 1
		print images_by_city
		if count > 0:
			center[0] /= count
			center[1] /= count
			print center
		else:
			center = None
		return render_template("world_map.html", name=json.dumps(username), locations=locations, all_images=images_by_city, center=center)

@app.route('/walls', methods=["GET"])
def wall():
	username = request.args.get("name")
	lat = request.args.get("lat")
	lon = request.args.get("lon")
	print username
	print lat
	print lon
	
 	data = useInstaTrip.useInsta(username)
	data = data[1 : N]
	target_data = {}
	print len(data)
	for d in data:
		if "latitude" not in d or "longitude" not in d:
			continue
#		print "h1", d["latitude"]
#		print "h2", d["longitude"]
#		print "hello", abs(float(lon)-float(d["longitude"]))
#		print "hi", abs(float(lat)-float(d["latitude"]))
#		if abs(float(lon)-float(d["longitude"])) < 1 and abs(float(lat)-float(d["latitude"])) < 1:
#			key = "%d-%d" % (d["latitude"], d["longitude"])
#			target_data[key] = d
 	print target_data.keys()
 	return render_template("wall.html", name=json.dumps(username), data=target_data.values())

if __name__ == '__main__':
		app.debug = True
		app.run()
