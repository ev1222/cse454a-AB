from Product import Product
from Grits import Grits
from Customer import Customer
from Supplier import Supplier
from Lane import Lane

grits = Grits()

crete = Supplier("crete", grits, 15.28, 8000)

z1bv = Customer("01bv", grits, 20000)

lane1 = Lane(crete, z1bv)
print(lane1.getGrossShippingCost())