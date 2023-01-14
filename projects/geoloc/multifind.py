from geopy.geocoders import Nominatim
import numpy as nmp
arr = nmp.array( [ [1, "18 Gattinelli Lugo", 48022], [2, "36 Fiumazzo Lugo", 48022] ] )
a = len(arr)
geolocator = Nominatim(user_agent="your_app_name")

for i in arr:
    localizz = i[1]+", "+i[2]
    location = geolocator.geocode(localizz)
    print((location.latitude, location.longitude))

