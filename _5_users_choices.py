# from _1_food_details import *
# from sqlite3 import OperationalError

from operations2 import Operations
from _3_execute_operations import *
from _4_user_register_and_login import *


class user:
    history = []

    def __init__(self):
        self.obj = Operations()
    
    def menu_card(self):
        self.result = self.obj.viewMenu()


    def place_new_order(self):

        print("To order, enter the numbers only from the given menu! ")
        self.orders = input("Enter the no :  \n")

        lst_ord = list(self.orders)
        print(lst_ord)              

        print("Your Order :")
        order_items = []
        
        food_names = [Operations.getName(food_id) for food_id in lst_ord]
        print(food_names)


    def order_history(self):
        print("Here are your previous orders : ")
        print(self.history)


    def update_profile(self):
        users_profile.clear()
        users_profile.append({
            "full_name" : input("Your full name : "),
            "cell_no" : input("Enter your new 10 digit phone number : "),
            "email" : input('Enter the mail id : '),
            "address" : input("Enter your new address : "),
            "password" : input("Enter the new password : ")})     

        print("Your profile has been updated successfully.")
        print(users_profile)
    

    def next_visit(self):
        pass
        
            
 



