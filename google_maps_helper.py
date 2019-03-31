import urllib.request, urllib.parse
import collections
import geocoder
from json import load

class GoogleMapsHelper():
    def __init__(self):
        '''
        Initializes GoogleMapsHelper class with api_key from credentials json file and sets url for distance matrix api.
        '''
        with open("credentials.json") as f:
            creds = load(f)
        self.api_key = creds["google"]["api_key"]
        self.url_distance = "https://maps.googleapis.com/maps/api/distancematrix"

    def build_url_dist(self, dest: str, origin: str) -> str:
        '''
        Builds the URL for the DistanceMatrix API by taking in a destination and origin. Returns a URL string.
        '''
        query_param = [('units', 'imperial'), ('origins', origin), ('destinations', dest), ('key', self.api_key)] # Unit set to imperial
        return self.url_distance + '/json?' + urllib.parse.urlencode(query_param)

    def get_dist(self, url: str) -> dict:
        '''
        Handles URL request response and returns a dictionary of the json response if accepted.
        '''
        response = None
        try:
            response = urllib.request.urlopen(url)
            return load(response)
        finally:
            if response != None:
                response.close()

    def get_min(self, locations: list) -> list:
        '''
        Given a list of locations, returns a list of sorted distances from closest to farthest by using the DistanceMatrix API.
        '''
        latlong = self.getLocation()
        origin = str(latlong[0]) + ", " + str(latlong[1])
        distances = dict()
        for location in locations:
            try:
                url = self.build_url_dist(location, origin)
                dist = self.get_dist(url)
                distances[location] = float(dist["rows"][0]["elements"][0]["distance"]["text"].strip(" mi").replace(",", ""))
            except:
                pass
        sorted_distances = sorted(distances.items(), key=lambda kv: kv[1])
        if(sorted_distances is None):
            return None
        i = 0
        min = []
        for item in sorted_distances:
            min.append(item)
            i += 1
            if i == 3:
                break
        return min

    def getLocation(self):
        '''
        Finds latitude and longitude given user's IP address.
        '''
        return geocoder.ip('me').latlng
