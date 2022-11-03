from dataclasses import dataclass, field
from typing import List
from Product import Product

@dataclass
class Customer():
    name: str
    loc: str
    products: List[Product]
    #type = type(product)

    def __post_init__(self):
        self.demand = len(self.products)