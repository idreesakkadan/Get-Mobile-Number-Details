import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

phone_number = input('ENTER THE MOBILE NUMBER WITH YOUR COUNTRY CODE:')

ch_number = phonenumbers.parse(phone_number, "CH")
print(geocoder.description_for_number(ch_number, "de"))
ro_number = phonenumbers.parse(phone_number, "RO")
print(carrier.name_for_number(ro_number, "en"))
