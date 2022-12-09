# data shapes
# Product: name, supplier, cost
#  -> products(dictionary): [key=product_name, value=list of Product]
# Lane: customer, supplier, transport cost, product
#  -> lanes(list): list of Lane
# Customer: name, product_demand(list of tuples)
#  -> customers_dict(dictionary): [key=customer_name, value=list of (product_name, demand)]
#  -> customers(list): list of Customer
# supplier: name, product_capacity(list of tuples)
#  -> suppliers_dict(dictionary): [key=supplier_name, value=list of (Product, capacity)]
#  -> suppliers(list): list of Supplier




import pandas as pd
from dataclasses import dataclass

from Product import Product
from Customer import Customer
from Supplier import Supplier
from Lane import Lane

from DE95 import DE95
from HFCS import HFCS
from Grits import Grits

from Optimizer import optimize
from GenerateCSV import generateCSV

source_file = "NAZ CornDataBook 9.7 09 27.xlsx"
xlsx = pd.ExcelFile(source_file)

grits = Grits()
de95 = DE95()
hfcs = HFCS()
prod_list = [grits, hfcs, de95]

        
def getProducts() :
    production_cost_data = pd.read_excel(xlsx, 'Production Cost')
    production_cost_data.drop_duplicates(subset=["Supplier Name","Product Name"], keep="last", inplace=True)    
    production_cost_data = production_cost_data.iloc[:,1:4]
    
    products = []
    for i, row in production_cost_data.iterrows() :
        products.append(Product(row["Product Name"], row["Supplier Name"], row["Production Cost (EXW)"]))

    return products

def getCustomers() :
    customers_demand_data = pd.read_excel(xlsx, 'Customers Demand')
    customers_demand_data.drop_duplicates(subset=["Customer Name","Product Name"], keep="last", inplace=True)
    customers_demand_data = customers_demand_data.iloc[:, [2,3,5]]
    
    customers = []
    for i, row in customers_demand_data.iterrows() :
        customers.append(Customer(row["Customer Name"], row["Product Name"], row["Base Demand"]))

    # print(customers)
        
    return customers

def getSuppliers(products) :
    suppliers_capacity_data = pd.read_excel(xlsx, 'Suppliers Capacity')
    suppliers_capacity_data.drop_duplicates(subset=["Supplier Name","Product Name"], keep="last", inplace=True)
    suppliers_capacity_data = suppliers_capacity_data.iloc[:, [2,4,7]]

    suppliers = []
    for i, row in suppliers_capacity_data.iterrows() :
        curr_prod = next(
              (prod for prod in prod_list if prod.name == row["Product Name"]), # and prod.supplier_name == row["Supplier Name"]),
              None
        )
        
        prod_cost = next(
            (prod.weight for prod in products if prod.size == row["Supplier Name"]
            and prod.name == row["Product Name"]), 
            None
        )

        suppliers.append(Supplier(row["Supplier Name"], curr_prod, prod_cost, row["Capacity (contracted for ABI)"]))

    # print(suppliers) 

    return suppliers

def getLanes(customers, suppliers) :
    transportation_cost_data = pd.read_excel(xlsx, 'Transportation Cost')
    transportation_cost_data = transportation_cost_data.iloc[:, [0, 1, 2, 5]]

    lanes = []
    for i, row in transportation_cost_data.iterrows() :
        curr_cust = next(
              (cust for cust in customers if cust.name == row["Site To"] and cust.product == row["Product Name"]),
              None
            )
        if curr_cust == None:
            continue

        curr_supp = next(
              (supp for supp in suppliers if supp.name == row["Site From"] and supp.product.name == row["Product Name"]),
              None
            )
        if curr_supp == None:
            continue

        lanes.append(Lane(f'lane{i}', curr_cust, curr_supp, row["Transportation Cost"]))

    # print(lanes)

    return lanes

# demo
products = getProducts()
customers = getCustomers()
suppliers = getSuppliers(products)
lanes = getLanes(customers, suppliers)

sc = optimize(lanes)

generateCSV(sc)