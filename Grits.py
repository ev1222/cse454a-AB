from Product import Product
from dataclasses import dataclass, field

@dataclass
class Grits(Product):
    size: float = field(default=0.5) # sq in ? doesn't really matter rn
    weight: float = field(default=1) # lbs