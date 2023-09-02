import re

users_profile = []

def register():
    full_name = input("Enter your full name : ")
    users_profile.append(full_name)
    phone_no()
    mail()
    address = input("Enter your present address : ")
    users_profile.append(address)
    Password()

def phone_no():
    cell_no = input("Enter your 10 digit phone number : ")
    pattern = r'\A[1-9]{1}[0-9]{9}\Z'
    res = re.findall(pattern, cell_no)
    if res:
        print("Your cell number is considered valid.")
        users_profile.append(cell_no)
    else:
        print("Enter a valid phone number")
        phone_no()

def mail():
    email = input('Enter the mail id : ')
    pattern = r'^[\w\.-]+@[a-z]+\.[a-z]{2,5}$'          
    res = re.findall(pattern, email)
    if res:
        print("Your mail id is valid.")
        users_profile.append(email)
    else:
        print("Enter a valid mail id.")
        mail()

def Password():
    print("The password must contain atleast 8 characters with 2 lowercase, 2 uppercase, 2 numbers and 2 special characters.")
    password = input("Enter the password : ")
    pattern = r'\A(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&8=+])(?!.*\s).{8,16}\Z'
    res = re.findall(pattern, password)                                            
    if res:
        print("This password is valid. ")
        print("\nRegistration Successful !")
        users_profile.append(password)
    else:
        print("Enter appropriate password, this is invalid. ")
        Password()


def login():
    print("\nLogin and complete the process !")
    enter_mail = input("Enter your registered email-id : ")
    enter_password = input("Enter your set password : ")
    if enter_mail in users_profile:
        if enter_password in users_profile:
            print("\nLogin Successful ! Be ready to fill your stomach with delicious serves !.")
            
        else:
            print("\nYour password doesn't match the registered ones, enter correct one.")
            login()                        
    else:
        print("\nThe email-id is invalid, Enter the appropriate one.")
        login()               


print("                          ~ WELCOME TO THE FOOD WORLD !! ~")
print("\nTo receive our servies, please do 'Register' and 'Login', following the mentioned rules. ")


print("\nEnter your choice to go further.")
choice = {1:"Press 1 for Registration", 2:"Press 2 for Login"}        
for value in choice:
    print('\n', str(value)+'.',choice[value])     
choice_input = int(input("Enter the no. : "))
if choice_input == 1:
    register()
elif choice_input == 2:
    login()
else:
    print("Exit") 


print("\nTo register for new user , type 1, or to login type 2.")
n = int(input("Enter the number : "))
if n == 1:
    register()
    print("\nTo login type 1 or exit the page")
    a = int(input("enter the response : "))
    if a == 1:
        login()
    else:
        print("Thank You ! Do visit Again.")
elif n == 2:
    login()
else:
    print("Exit")

class access:
    def __init__(self,full_name, cell_no, email, address, password):
        self.full_name = full_name
        self.cell_no = cell_no 
        self.email = email
        self.address = address
        self.password = password