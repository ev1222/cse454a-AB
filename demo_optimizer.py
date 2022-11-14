from Product import Product
from Grits import Grits
from Customer import Customer
from Supplier import Supplier
from Lane import Lane
from SupplyChain import SupplyChain
from Optimizer import optimize
from GenerateCSV import generateCSV

grits = Grits()

crete = Supplier("Crete", grits, 15.28, 20000)
danville = Supplier("Danville", grits, 15.61, 40000)
dmilling = Supplier("Didion Milling", grits, 14.29, 20000)

z1bv = Customer("01bv", grits, 20000)
z1cv = Customer("01cv", grits, 34000)

lane1 = Lane("lane1",z1bv, crete, 400)
lane2 = Lane("lane2",z1bv, dmilling, 500)
lane3 = Lane("lane3",z1cv, danville, 500)

lanes = [lane1, lane2, lane3]

sc = optimize(lanes)

if sc.isValid():
    success, error_msg = generateCSV(sc)
    if success:
        print('CSV file successfully generated/updated')
    else:
        print(error_msg)
else:
    print('Supply Chain is not valid')