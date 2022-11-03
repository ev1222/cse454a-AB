from dataclasses import dataclass, field
from Product import Product
from typing import List

@dataclass
class Supplier():
    name: str
    #loc: str
    product: Product
    prod_cost: float #per item
    capacity: int
    
    def __post_init__(self):
        self.total_prod_cost = self.capacity*self.prod_cost

