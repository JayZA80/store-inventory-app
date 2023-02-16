class item:
    def __init__(self, name, price, stock, desc):
        self.name = name
        self.price = price
        self.stock = stock
        self.desc = desc
    def showItem(self):
        print(f"Your created item: {self.name}, ${self.price}, {self.stock} count, {self.desc}" )

name = None
while not name: 
    name = input("Put the name of the item: ")
price = None
while not price:
    price = input("Type the price of one item: ")
stock = None
while not stock:
    stock = input("How many do you currently have: ")
desc = None
while not desc:
    desc = input("Provide a short description: ")

item1 = item(name, price, stock, desc)

item1.showItem()