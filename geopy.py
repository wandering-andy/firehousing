from geopy.geocoders import Nominatim
import csv

# Set up the geocoder
geolocator = Nominatim(user_agent="my_app")

# Read the addresses from the file
addresses = []
with open("addresses.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        addresses.append(row[0])

# Geocode the addresses and retrieve the longitudes and latitudes
results = []
for address in addresses:
    location = geolocator.geocode(address)
    if location:
        longitude = location.longitude
        latitude = location.latitude
        results.append((address, longitude, latitude))

# Print the results
for result in results:
    address, longitude, latitude = result
    print(f"Address: {address}")
    print(f"Longitude: {longitude}")
    print(f"Latitude: {latitude}")
    print()