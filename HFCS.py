from Product import Product
from dataclasses import dataclass, field

@dataclass
class HFCS(Product):
    name: str = field(default = 'HFCS')
    size: float = field(default=0.5) # sq in ? doesn't really matter rn
    weight: float = field(default=1) # lbs