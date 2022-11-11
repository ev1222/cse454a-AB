from dataclasses import dataclass, field
from Product import Product
from typing import List

#TODO: Suppliers can be supplying multiple products. 
# Need to implement this and update the rest of objects to match. 

@dataclass
class Supplier():
    name: str
    #loc: str
    product: Product
    prod_cost: float #assumed per 100 lbs
    capacity: int
    
    def __post_init__(self):
        self.total_prod_cost = ((self.capacity*self.product.weight)/100) * self.prod_cost

