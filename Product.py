from dataclasses import dataclass
from abc import ABC

@dataclass
class Product(ABC):
    size: float
    weight: float