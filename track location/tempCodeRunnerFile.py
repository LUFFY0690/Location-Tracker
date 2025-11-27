import phonenumbers
from myphone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse("9816623847")
location = geocoder.description_for_number(pepnumber, "en")
print(location)