from dataclasses import dataclass
from typing import List
from Customer import Customer
from Supplier import Supplier

#TODO: if need be, implement more granular calculations of transport cost
@dataclass
class Lane(): 
    suppliers: List[Supplier]
    customer: Customer
    #transport_cost: float #per 100 lbs

    #TODO: eventually make this able to lookup from dataset transport cost
    def __post_init__(self):
        self.transport_cost = 6.95

    def getGrossShippingCost(self) -> float:
        for supplier in self.suppliers:
            total_prod_weight = supplier.capacity * supplier.product.weight
            gross_shipping_cost = total_prod_weight/100 * self.transport_cost
            return gross_shipping_cost

    def isValid(self):
        pass