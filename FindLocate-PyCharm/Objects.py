from cmd import PROMPT
from phonenumbers import carrier
from phonenumbers.phonenumber import PhoneNumber
from main import located, service_pro, LookUpNumber

first_name = input("Please enter your first name: ")
last_name = input("please enter your last name: ")
age = int(input("please enter your age: "))
gender = input("Please enter your gender: ")
nationality = input("Please enter your nationality: ")
passWord =  input("Please create a password: ")
confirm_password = input("Please confirm your password: ")

class UserDetail:
   def __init__(self, first_name, last_name, age, gender, nationality):
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
       self.gender = gender
       self.nationality = nationality



fullname = f"{first_name} {last_name}"
UserAge = age
UserTel = LookUpNumber
service_provider = carrier.name_for_number(service_pro,"en")
user_location = located

while passWord != confirm_password:
    print("please make sure that your password match")
    confirm_password = input("Please confirm your password: ")

print("Successful creation of password")
loggedIn = False

while not loggedIn:
    user_input = input("Please enter your password: ")
    if passWord == user_input:
        print(f"log in successful. Welcome {first_name} {last_name}")

        loggedIn = True
    else:
        print("incorrect LogIn. Please enter your pass word again")
        user_input = input(
            "Please enter your password: ")  # for everytime the user enters the wrong password,the program will re-assign the user_input variable to ensure that the variable always holds a password enters most recent


#this class wil be store the firstname and lastname of the user and when called, it will display their location as well as their full details
class UserLocate:
    def __init__(self, fullname, UserAge, UserTel, service_provider, user_location, confirm_password):
        self.Fullname = fullname
        self.Age = UserAge
        self.Tel = UserTel
        self.serviceProvider = service_provider
        self.UserLocation = user_location
        self.confirm_password = confirm_password

    def display_info(self):
        print(f"Name: {self.Fullname}")
        print(f"Age: {self.Age}")
        print(f"Phone number: {self.Tel}")
        print(f"Service provider: {self.serviceProvider}")
        print(f"Location: {self.UserLocation}")
        print(f"password: {confirm_password}")

CallBack = UserLocate(fullname, UserAge, UserTel, service_provider,user_location, confirm_password)
CallBack.display_info()






