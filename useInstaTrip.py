#!/usr/bin/python
# ordering imports

# self written module
import trip
import igram as insta
import keys

def useInsta(insta_userid):
    uid = insta.get_ig_userid(insta_userid)
    photo_list = insta.get_recent_photos(uid)

    for photo in photo_list:
        lat = photo['latitude']
        lon = photo['longitude']
        name = ['placename']

        location_id = trip.getAttractions(lat,lon,nam)
        reviews_and_urls = trip.getReviews(location_id)

        photo.update(reviews_and_urls)

def main():
    #TEST
    userid = "mattbg"
    useInsta(useInsta)

if __name__ == "__main__":
    main()
