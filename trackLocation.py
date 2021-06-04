# Program to find region
# of a phone number
import phonenumbers
from phonenumbers import geocoder
  
# Parsing String to Phone number
phoneNumber = phonenumbers.parse("+919876543210")
  
# Getting region information
Region = geocoder.description_for_number(phoneNumber, 'en')
  
# Printing the region of a phone number
print(Region)
