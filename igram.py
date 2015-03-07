import json
import requests

ig_client_id = "c093bedbc7c64d04a3b28dd1c1fa72db"

def get_ig_userid(ig_username):
	url = "https://api.instagram.com/v1/users/search?q=" + ig_username + "&client_id=" + ig_client_id
	re = requests.get(url)
	da = json.loads(re.text)
	for u in da["data"]:
		if u["username"]==ig_username:
			return u["id"]
	return 0

def get_recent_photos(ig_userid):
	url = "https://api.instagram.com/v1/users/" + ig_userid + "/media/recent/?client_id=" + ig_client_id
	re = requests.get(url)
	da = json.loads(re.text)
	photos = []
	for p in da['data']:
		if (p['location'] and p['location'].get('name')):
			pdata = {}
			pdata['timestamp']=p['caption']['created_time']
			pdata['latitude']=p['location']['latitude']
			pdata['longitude']=p['location']['longitude']
			pdata['placename']=p['location']['name']
			pdata['thumbnail']=p['images']['thumbnail']['url']
			pdata['imageurl']=p['images']['low_resolution']['url']
			print pdata
			photos.append(pdata)
	return json.dumps(photos)

uid = get_ig_userid("mattbg")
print uid
ps = get_recent_photos(uid)
print ps



