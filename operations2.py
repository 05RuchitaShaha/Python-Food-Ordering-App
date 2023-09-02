from _1_food_details import *


class Operations:
    food_menu = []

    def addFoodItem(self):
        FoodID = int(input("Enter the food ID : "))
        Name = input("Enter the item name : ")
        Quantity = input("Enter the serving quantity : ")
        Price = input("Enter the price : ")
        Discount = float(input("Enter the discount (calculated in %) : "))
        Stock = input("Enter the stock available : ")
        food_obj = Food(FoodID = FoodID, Name = Name, Quantity = Quantity, Price = Price, Discount = Discount, Stock = Stock)
        self.food_menu.append(food_obj)
        print(f"The food item with ID {FoodID} has been successfully added in the menu.")

    def editFoodItem(self):
        ID = int(input("Enter the ID you want to edit : "))
        for items in self.food_menu:
            if items.get_FoodID() == ID:
                Name = input("Enter the item name : ")
                Quantity = input("Enter the serving quantity : ")
                Price = input("Enter the price : ")
                Discount = float(input("Enter the discount (calculated in %) : "))
                Stock = input("Enter the stock available : ")
                items.set_Name(Name)
                items.set_Quantity(Quantity)
                items.set_Price(Price)
                items.set_Discount(Discount)
                items.set_Stock(Stock)
                break
        else:
            print("The given food ID is not present in the menu.")

    def viewFoodItem(self):
        for items in self.food_menu:
            print(items,'\n')
        
    
    def removeFoodItem(self):
        ID = int(input("Enter the ID you want to edit : "))
        for items in self.food_menu:
            if items.get_FoodID() == ID:
                self.food_menu.remove(items)
                print("The respective item has been removed successfully.")
                break
        else:
            print("The given food ID is not present in the menu.")

    def __str__(self):
        pass


    def viewMenu(self):
        for index, food_item in enumerate(self.food_menu):
            self.menu = f"{index+1}. {food_item.Name} ({food_item.Quantity}) [INR {food_item.Price}]"
            print(self.menu)
            

    @classmethod    
    def getName(self, food_id):

        for item in self.food_menu:
            if item["FoodID"] == food_id:
                return item["Name"]
        return None

        

