class Item:
    def __init__(self, name, price, stock, cond):
        self.name = name
        self.price = price
        self.stock = stock
        self.condition = cond

class Clothing(Item):
    def __init__(self, name, price, stock, cond, size):
        super().__init__(name, price, cond, stock)
        self.size = size

class Figure(Item):
    def __init__(self, name, price, stock, scale, manu, cond):
        super().__init__(name, price, cond, stock)
        self.scale = scale
        self.manu = manu