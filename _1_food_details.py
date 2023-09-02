class Food:
    def __init__(self, FoodID, Name, Quantity, Price, Discount, Stock):
        self.FoodID = FoodID
        self.Name = Name
        self.Quantity = Quantity
        self.Price = Price
        self.Discount = Discount
        self.Stock = Stock
    
    def __str__(self):
        return f'Food ID : {self.FoodID}\nItem : {self.Name}\nQuantity : {self.Quantity}\nPrice : {self.Price}\nDiscount : {self.Discount}\nStock : {self.Stock}'

    def get_FoodID(self):
        return self.FoodID
    def set_FoodID(self, FoodID):
        self.FoodID = FoodID

    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name

    def get_Quantity(self):
        return self.Quantity
    def set_Quantity(self, Quantity):
        self.Quantity = Quantity

    def get_Price(self):
        return self.Price
    def set_Price(self, Price):
        self.Price = Price

    def get_Discount(self):
        return self.Discount
    def set_Discount(self, Discount):
        self.Discount = Discount

    def get_Stock(self):
        return self.Stock
    def set_Stock(self, Stock):
        self.Stock = Stock

