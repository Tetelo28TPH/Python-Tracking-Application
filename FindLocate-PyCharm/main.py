import folium
import phonenumbers
import geocoder
import opencage
from geopy.geocoders import Nominatim
from phonenumbers import carrier
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode

from phonenumbers.phonenumber import PhoneNumber

#boolean variable set to false. when the variable is true then the loop terminates
is_valid = False
while not is_valid:
    phoneNumber = input("Please enter your phone number: ")

    try:
     #The phone number is turned into a phone number object. This object (Phonenumbers) is a special python library
        LookUpNumber = phonenumbers.parse(phoneNumber)
        if phonenumbers.is_valid_number(LookUpNumber):
            is_valid = True
    except Exception as e:
        print('Error occurred:',e)
        print('Please re-enter a valid phone number')

location = geocoder.description_for_number(LookUpNumber,"en")
print(location)

#It's going to look for the network provider if the user's phone number

service_pro = phonenumbers.parse(phoneNumber)
print(carrier.name_for_number(service_pro,"en"))

key = 'baf4683aa13243ae8c2d9bc52dede1a4'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)


if results:
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']
            coordinates = (lat,lng)

            precise_location = Nominatim(user_agent="location_app")
            located = precise_location.reverse(coordinates)
            print(f"your location is: {located.address}")


            myMap = folium.Map(location=coordinates, zoom_start=9)
            folium.Marker(location=coordinates, popup=located.address).add_to(myMap)
            myMap.save("myLocation.html")

else:
        print("could find coordinates for this region")


"""
import geopy.geocoders
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercies")

place = input("Enter City Name: ")

location = geolocator.geocode(place)

print(location)
"""



