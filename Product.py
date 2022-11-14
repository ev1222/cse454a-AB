from dataclasses import dataclass
from abc import ABC

@dataclass
class Product(ABC):
    name: str
    size: float
    weight: float