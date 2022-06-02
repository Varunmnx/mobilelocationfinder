import phonenumbers
from phonenumbers import carrier, geocoder, timezone


def findthenumber(mobileNo):
   print("Is number valid:",phonenumbers.is_valid_number(mobileNo))
   print("Time Zone:", timezone.time_zones_for_number(mobileNo))
   print("Carrier Name:",carrier.name_for_number(mobileNo,"en"))
   print("Location:",geocoder.description_for_number(mobileNo,"en"))

mobileNo=input("Enter mobile number with courntry code:") 
mobileNo=phonenumbers.parse(mobileNo)
findthenumber(mobileNo)
print("".join("*")*20)
print("created by Varunmx!!!")