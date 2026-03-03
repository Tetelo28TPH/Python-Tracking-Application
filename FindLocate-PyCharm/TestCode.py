
"""
Installation of required packages.
geopy: Used for the geocoding (converting locations into coordinates)
geocoder: Used to get geolocation data, like IP-Based location
"""
import geocoder
# pip install geopy
# pip install geocoder

"""
Importing geopy libraries
geopy: main package for geocoding
nominatim: A geocoding service provided by OpenStreetMap, used to look up geographic coordinates from location names
"""
import geopy
from geopy.geocoders import Nominatim

"""
geocoder.ip ('me'): tries to get the the user's location using using their IP address.
g.latlng: Returns a list with the latitude and longitude.

approximate location based on IP BUT Function may be inaccurate depending on ISP, VPNs, etc.
"""

g = geocoder.ip('me')
print("Your Location is:")
print(g.address)

def get_user_location():
    geolocator = Nominatim(user_agent="location_app")
    user_location = None

#User is asked to enter location. The loop is terminated only when the 'user_location is None' is no longer true.
    # meaning if i enter a correct city name, the location will be stored the 'user_location' and the loop is terminated
    #if I enter the wrong city, the user will be prompted till a valid city  name is entered
    while user_location is None:
        user_input = input("Please enter the location you want (city, country, etc.): ")
        try:
            user_location = geolocator.geocode(user_input)
        except Exception as e:
            print("Error occurred:", e)
            print("Please try again.")
            
    print(f"Your location is: {user_location}")
    print("Your GPS coordinates:")
    print(f"Latitude: {user_location.latitude}")
    print(f"Longitude: {user_location.longitude}")

#the if statement makes sure that the function defined above is only executed in the main file its defined
 #meaning it will not run in an imported file
if __name__ == "__main__":
    get_user_location()