import requests
import pdb

API_KEY = "AIzaSyDQomw3vxOR3GjusU49isg-fxFMEWN29LA"

GEOCODE_API_KEY = "AIzaSyDyhP6D3CqQAYLum8qWPS8IYGk1Kc_2AXg"

BASE_URL = "https://maps.googleapis.com/maps/api/streetview?size=400x400&location="

GEOSEARCH_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json?"



class ImageFinder:
    @staticmethod
    def get_images_by_lat_lng(latitude = 40.720032, longitude = -73.988354):
        image = requests.get(BASE_URL + str(latitude) + ", " + str(longitude) + "&key=" + API_KEY)
        return image

    @staticmethod
    def get_images_by_zipcode(zipcode = 11209):
        latitude, longitude = ImageFinder.get_coordinates_from_zipcode(zipcode)
        image = requests.get(BASE_URL + str(latitude) + ", " + str(longitude) + "&key=" + API_KEY)
        return image

    @staticmethod
    def get_coordinates_from_zipcode(zipcode = 11209):
        geo_response = requests.get(GEOSEARCH_BASE_URL + "address=" + str(zipcode) + "&key=" + GEOCODE_API_KEY)
        if geo_response.status_code == 200:
            geo_result = geo_response.json()['results'][0]
            geo_result = geo_result if geo_result != None else {}
            coordinates = geo_result['geometry']['location']
            return (coordinates['lat'], coordinates['lng'])
