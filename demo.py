from Product import Product
from Grits import Grits
from Customer import Customer
from Supplier import Supplier
from Lane import Lane
from SupplyChain import SupplyChain

grits = Grits()

crete = Supplier("Crete", grits, 15.28, 8000)
danville = Supplier("Danville", grits, 15.61, 134400)
dmilling = Supplier("Didion Milling", grits, 14.29, 67304)

z1bv = Customer("01bv", grits, 20000)
z1cv = Customer("01cv", grits, 34000)

lane1 = Lane("lane1",z1bv)
lane1.addSupplier(crete)
lane1.addSupplier(danville)

lane2 = Lane("lane2",z1cv)
#lane2.addSupplier(dmilling)
#lane2.addSupplier(crete)

sc = SupplyChain("sc1")
sc.addLane(lane1)
sc.addLane(lane2)

if not sc.isValid():
    print("Uh oh!")
print("Total cost of supply chain:")
print(f'${round(sc.grossCost(),2):,}')