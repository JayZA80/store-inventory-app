from item import *
from itemUpdater import *

item1 = Item('Test', 19.99, 5, 'S')

item1.stock = addQty(item1.stock)

print(item1.stock)