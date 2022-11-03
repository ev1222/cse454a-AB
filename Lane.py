from dataclasses import dataclass, field
from typing import List
from Customer import Customer
from Supplier import Supplier

#TODO: if need be, implement more granular calculations of transport cost
@dataclass
class Lane(): 
    customer: Customer

    def __post_init__(self):
        self.transport_cost: dict[Supplier, float] = {"crete":6.95, "danville":4.96} # per 100 lbs
        self.suppliers: List[Supplier] = []

    def addSupplier(self,supplier):
        self.suppliers.append(supplier)

    def getGrossShippingCost(self) -> float:
        gross_shipping_cost = 0
        for supplier in self.suppliers:
            total_prod_weight = supplier.capacity * supplier.product.weight
            gross_shipping_cost += total_prod_weight/100 * self.transport_cost[supplier.name]
        return gross_shipping_cost

    def getGrossProductionCost(self) -> float:
        gross_production_cost = 0
        for supplier in self.suppliers:
            gross_production_cost += supplier.total_prod_cost
        return gross_production_cost
    
    def getLaneCost(self) -> float:
        return self.getGrossProductionCost() + self.getGrossShippingCost()

    def isValid(self):
        pass