from geopy.geocoders import Nominatim

# create a Nominatim object
geolocator = Nominatim(user_agent="your_app_name")
#location = geolocator.geocode("121 N LaSalle St, Chicago")
location = geolocator.geocode("18 Gattinelli Lugo, 48022")

#print(location.raw)
#print(location.address)
print((location.latitude, location.longitude))