from Product import Product
from Customer import Customer
from Supplier import Supplier
from Lane import Lane

grits = Product("grits",0.5,1)

crete_supply = [grits] * 8000
crete = Supplier("crete", "n/a", crete_supply, 15.28)

z1bv_demand = [grits] * 20000
z1bv = Customer("01bv","n/a",z1bv_demand)

lane1 = Lane(crete, z1bv)
#print(lane1.get_gross_shipping_cost())