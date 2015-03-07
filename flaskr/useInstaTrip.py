#!/usr/bin/python
# ordering imports

# self written module
import trip
import igram as insta
import copy

def useInsta(insta_userid):
    userid = copy.copy(insta_userid)
    uid = insta.get_ig_userid(userid)
    photo_list = insta.get_recent_photos(uid)

    for photo in photo_list:
        lat = photo['latitude']
        lon = photo['longitude']
        name = photo['placename']

        location_id = trip.getAttractions(lat,lon,name)
        reviews_and_urls = trip.getReviews(location_id)
        
        photo.update(reviews_and_urls)
        
        print photo

def main():
    #TEST
    userid = "mattbg"
    useInsta(userid)

if __name__ == "__main__":
    main()
