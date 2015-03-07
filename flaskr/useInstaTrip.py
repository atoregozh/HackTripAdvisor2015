#!/usr/bin/python
# ordering imports

# self written module
import trip
import igram as insta
import copy

def useInsta(insta_userid, max_id):
	userid = copy.copy(insta_userid)
	uid = insta.get_ig_userid(userid)
	photo_page = insta.get_recent_photos(uid, max_id)
	
	for photo in photo_page['photos']:
		lat = photo['latitude']
		lon = photo['longitude']
		name = photo['placename']

		location_id = trip.getAttractions(lat,lon,name)
		reviews_and_urls = trip.getReviews(location_id)
		
		photo.update(reviews_and_urls)
	return photo_page

def main():
    #TEST
    userid = "mattbg"
    print useInsta(userid, None)

if __name__ == "__main__":
    main()
