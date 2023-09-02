# from sqlite3 import OperationalError
# from _1_food_details import *
from operations2 import *
from operations2 import Operations

class Main:
    def execute(self, choice, operations):
        if choice == 1:
            print("\n~ Add new Item ~")
            operations.addFoodItem()

        if choice == 2:
            print("\n~ Edit an Item ~")
            operations.editFoodItem()

        if choice == 3:
            print("\n~ View the Items ~")
            operations.viewFoodItem()

        if choice == 4:
            print("\n~ Remove an Item ~")
            operations.removeFoodItem()

        if choice == 5:
            print("\n~ No more Items ~")
            operations.__str__()
            

    def admin_login(self):
        print("\n# The ADMIN must login in to perform the functionalities. # \n")
        self.file = open("admin.txt", "r")
        data = self.file.read()
        print("Refer this : \n", data)

        self.admin_name = input("\nEnter your name : ")
        if self.admin_name in data:
            print("Go ahead !")
        else:
            print("Refer the given details.")
            main.admin_login()

        self.admin_password = input("\nEnter your registered password : ")
        if self.admin_password in data:
            print("\n@@ WELCOME TO OUR CAFE ! @@")
        else:
            print("Refer the given details.")
            main.admin_login()


if __name__ == "__main__":
    operations = Operations()
    main = Main()
    
    main.admin_login()
    while True:
        choice = int(input("\nEnter the Number to :\n1.Add Item \n2.Edit Item \n3.View Items \n4.Remove Item\n5.No More Item\n"))
        main.execute(choice,operations)
        if choice == 5:
            print(" IT's CUSTOMER's CHOICE !! \n")
            break
            

