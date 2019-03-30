import urllib.request, urllib.parse
import collections
import geocoder
from json import load

class GoogleMapsHelper():
    def __init__(self):
        with open("credentials.json") as f:
            creds = load(f)
        self.api_key = creds["google"]["api_key"]
        self.url_distance = "https://maps.googleapis.com/maps/api/distancematrix"
        self.url_direction = "https://maps.googleapis.com/maps/api/directions"

    def build_url_dist(self, dest: str, origin: str) -> str:
        query_param = [('units', 'imperial'), ('origins', origin), ('destinations', dest), ('key', self.api_key)]
        return self.url_distance + '/json?' + urllib.parse.urlencode(query_param)

    def get_dist(self, url: str) -> dict:
        response = None
        try:
            response = urllib.request.urlopen(url)
            return load(response)
        finally:
            if response != None:
                response.close()

    def get_min(self, locations: list) -> list:
        latlong = self.getLocation()
        origin = str(latlong[0]) + ", " + str(latlong[1])
        distances = dict()
        for location in locations:
            url = self.build_url_dist(location, origin)
            dist = self.get_dist(url)
            distances[location] = float(dist["rows"][0]["elements"][0]["distance"]["text"].strip(" mi").replace(",", ""))
        sorted_distances = sorted(distances.items(), key=lambda kv: kv[1])
        return sorted_distances

    def getLocation(self):
        return geocoder.ip('me').latlng
