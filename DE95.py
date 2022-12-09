from Product import Product
from dataclasses import dataclass, field

@dataclass
class DE95(Product):
    name: str = field(default = 'DE95')
    size: float = field(default=0.5) # sq in ? doesn't really matter rn
    weight: float = field(default=1) # lbs