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

source_file = "NAZ CornDataBook 9.7 09 27.xlsx"
xlsx = pd.ExcelFile(source_file)

# @dataclass
# class Product():
#     name: str
#     supplier_name: str
#     cost: float

#     def __init__(self, name, supplier_name, cost) :
#       self.name = name
#       self.supplier_name = supplier_name
#       self.cost = cost

# @dataclass
# class Customer():
#     name: str
#     product: Product
#     demand: float
        
#     def __init__(self, name, product, demand) :
#       self.name = name
#       self.product = product
#       self.demand = demand

# @dataclass
# class Supplier():
#     name: str
#     product: Product
#     capacity: int

#     def __init__(self, name, product, capacity) :
#       self.name = name
#       self.product = product
#       self.capacity = capacity

# @dataclass
# class Lane(): 
#     customer: Customer
#     supplier: Supplier
#     product: Product
#     transport_cost: float
        
#     def __init__(self, customer, supplier, product, transport_cost):
#         self.customer = customer
#         self.supplier = supplier
#         self.product = product
#         self.transport_cost = transport_cost
        
def getProducts() :
    production_cost_data = pd.read_excel(xlsx, 'Production Cost')
    production_cost_data.drop_duplicates(subset=["Supplier Name","Product Name"], keep="last", inplace=True)    
    production_cost_data = production_cost_data.iloc[:,1:4]
    
    products = []
    for i, row in production_cost_data.iterrows() :
        products.append(Product(row["Product Name"], row["Supplier Name"], row["Production Cost (EXW)"]))

    # print(products)

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
              (prod for prod in products if prod.name == row["Product Name"] and prod.supplier_name == row["Supplier Name"]),
              None
          )
        suppliers.append(Supplier(row["Supplier Name"], curr_prod, row["Capacity (contracted for ABI)"]))

    # print(suppliers) 

    return suppliers

def getLanes(customers, suppliers, products) :
    transportation_cost_data = pd.read_excel(xlsx, 'Transportation Cost')
    transportation_cost_data = transportation_cost_data.iloc[:, [0, 1, 2, 5]]

    lanes = []
    for i, row in transportation_cost_data.iterrows() :
      curr_cust = next(
              (cust for cust in customers if cust.name == row["Site To"] and cust.product == row["Product Name"]),
              None
            )
      curr_supp = next(
              (supp for supp in suppliers if supp.name == row["Site From"] and supp.product.name == row["Product Name"]),
              None
            )
      curr_prod = next(
              (prod for prod in products if prod.name == row["Product Name"] and prod.supplier_name == row["Site From"]),
              None
            )
      lanes.append(Lane(curr_cust, curr_supp, curr_prod, row["Transportation Cost"]))

    # print(lanes)

    return lanes

products = getProducts()
customers = getCustomers()
suppliers = getSuppliers(products)
lanes = getLanes(customers, suppliers, products)

print(products[0])
print(customers[0])
print(suppliers[0])
print(lanes[0])