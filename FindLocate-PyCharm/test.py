import phonenumbers
from phonenumbers.phonenumber import PhoneNumber

#User will be prompted to enter their phone numbers inorder to get their location
# phoneNumber = input("Please enter your phone number: ")

# #In the case the user enters does not enter valid phone, they will be prompted to enter their phone number again
# while user_location is None:
#     user_input = input("Please enter the location you want (city, country, etc.): ")
#     try:
#         user_location = geolocator.geocode(user_input)
#     except Exception as e:
#         print("Error occurred:", e)
#         print("Please try again.")
#
# print(f"Your location is: {user_location}")
# print("Your GPS coordinates:")
# print(f"Latitude: {user_location.latitude}")
# print(f"Longitude: {user_location.longitude}")
#
# if __name__ == "__main__":
#     get_user_location()


#boolean variable set to false. when the variable is true then the loop terminates
# is_valid = False
# while not is_valid:
#     phoneNumber = input("Please enter your phone number: ")
#
#     try:
#      #The phone number is turned into a phone number object. This object (Phonenumbers) is a special python library
#         LookUpNumber = phonenumbers.parse(phoneNumber)
#         if phonenumbers.is_valid_number(LookUpNumber):
#             is_valid = True
#     except Exception as e:
#         print('Error occurred:',e)
#         print('Please re-enter a valid phone number')

