from dataclasses import dataclass, field
from Product import Product
from typing import List

"""
class Supplier():
    def __init__(self, name, loc, product: Product, prod_cost) -> None:
        self.name = name
        self.loc = loc
        self.product = product
        self.products: List[Product]
        self.prod_cost = prod_cost
        #self.type = type(product)
        self.capacity = len(product)

    def total_prod_cost(self):
        return self.capacity*self.prod_cost
"""



@dataclass
class Supplier():
    name: str
    loc: str
    product: List[Product]
    prod_cost: float #per item

    def __post_init__(self):
        #self.type = self.get_type()
        self.capacity = len(self.product)

    def totalCost(self) -> float:
        return self.capacity*self.prod_cost

