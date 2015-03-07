#!/usr/bin/python
# ordering imports
# Standard Library modules
import json
import copy

# Third-party library
import requests

ig_client_id = "c093bedbc7c64d04a3b28dd1c1fa72db"

def get_ig_userid(ig_username):
	user = copy.copy(ig_username)
	url = "https://api.instagram.com/v1/users/search?q=" + user + "&client_id=" + ig_client_id
	re = requests.get(url)
	da = json.loads(re.text)
	for u in da["data"]:
		if u["username"]==user:
			return u["id"]
	return 0

def get_recent_photos(ig_userid):

	pages = []
	count = 0

	url = "https://api.instagram.com/v1/users/" + ig_userid + "/media/recent/?client_id=" + ig_client_id
	re = requests.get(url)
	da = json.loads(re.text)
	pages.extend(da['data'])
	while (da['pagination'].get('next_url') and count < 5):
		count+=1
		url = da['pagination']['next_url']
		re = requests.get(url)
		da = json.loads(re.text)
		pages.extend(da['data'])
	photos = []
	for p in pages:
		if (p['location'] and p['location'].get('name') and p['type']=="image"):
			pdata = {}
			#pdata['timestamp']=p['caption']['created_time']
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
