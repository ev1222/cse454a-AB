from Product import Product
from Grits import Grits
from Customer import Customer
from Supplier import Supplier
from Lane import Lane

grits = Grits()

crete = Supplier("crete", grits, 15.28, 8000)
danville = Supplier("danville", grits, 15.61, 134400)

z1bv = Customer("01bv", grits, 20000)

lane1 = Lane(z1bv)
lane1.addSupplier(crete)
lane1.addSupplier(danville)

print("Total cost of supply chain:")
print(f'${round(lane1.getLaneCost(),2):,}')