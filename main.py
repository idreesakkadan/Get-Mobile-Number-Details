import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

ch_number = phonenumbers.parse("+919526126856", "CH")
print(geocoder.description_for_number(ch_number, "de"))
ro_number = phonenumbers.parse("+919526126856", "RO")
print(carrier.name_for_number(ro_number, "en"))
