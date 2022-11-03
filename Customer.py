from dataclasses import dataclass, field
from typing import List
from Product import Product

@dataclass
class Customer():
    name: str
    #loc: str
    product: Product
    demand: int