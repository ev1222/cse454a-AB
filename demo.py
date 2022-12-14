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

lane1 = Lane("lane1",z1bv, crete, 500)
lane2 = Lane("lane2",z1bv, dmilling, 500)
lane3 = Lane("lane3",z1cv, danville, 500)


sc = SupplyChain("sc1")
sc.addLane(lane1)
sc.addLane(lane2)
sc.addLane(lane3)

if not sc.isValid():
    print("Uh oh!")
print("Total cost of supply chain:")
print(f'${round(sc.grossCost(),2):,}') # print output in rounded dollar format