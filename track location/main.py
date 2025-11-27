import phonenumbers
from phonenumbers import geocoder
from myphone import number
import folium



key = "1c181793e5214fdfb43cfbe5b6609403"
# Get location information
check_number = phonenumbers.parse(number)
number_loction = geocoder.description_for_number(check_number, "en")
print(number_loction)


#Get the sim card name
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))



from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(number_loction)
results = geocoder.geocode(query)

# Extracting latitude and longitude
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)



# Create a map using folium
map_location = folium.Map(location=[lat, lng], zoom_start=9)
# Add a marker to the map
folium.Marker([lat, lng], popup=number_loction).add_to(map_location)
# Save the map to an HTML file
map_location.save("mylocation.html")    
