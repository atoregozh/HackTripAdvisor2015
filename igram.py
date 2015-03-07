#!/usr/bin/python
# ordering imports
# Standard Library modules
import json

# Third-party library
import requests


# self written module
import keys

def get_ig_userid(ig_username):
	url = "https://api.instagram.com/v1/users/search?q=" + ig_username + "&client_id=" + keys.ig_client_id
	re = requests.get(url)
	da = json.loads(re.text)
	for u in da["data"]:
		if u["username"]==ig_username:
			return u["id"]
	return 0

def get_recent_photos(ig_userid):
	url = "https://api.instagram.com/v1/users/" + ig_userid + "/media/recent/?client_id=" + keys.ig_client_id
	re = requests.get(url)
	da = json.loads(re.text)
	photos = []
	for p in da['data']:
		if (p['location'] and p['location'].get('name')) and p['type']=="image":
			pdata = {}
			pdata['timestamp']=p['caption']['created_time']
			pdata['latitude']=p['location']['latitude']
			pdata['longitude']=p['location']['longitude']
			pdata['placename']=p['location']['name']
			pdata['thumbnail']=p['images']['thumbnail']['url'] #little image
			pdata['imageurl']=p['images']['low_resolution']['url']
			# print pdata
			photos.append(pdata)
	return photos

def main():
	#TEST cases
	uid = get_ig_userid("mattbg")
	print uid
	ps = get_recent_photos(uid)
	print ps

if __name__ == "__main__":
    main()



