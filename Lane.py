from typing import List
from Customer import Customer
from Supplier import Supplier

#TODO: if need be, implement more granular calculations of transport cost
class Lane(): 
    def __init__(self, customer: Customer):
        self.customer = customer
        self.transport_cost = dict() # per 100 lbs
        self.suppliers: List[Supplier] = []

    def addSupplier(self, supplier: Supplier):
        self.suppliers.append(supplier)
        self.transport_cost[supplier.name]=6.95 # hardcoded value for testing/demo purposes

    def removeSupplier(self, supplier: Supplier):
        self.suppliers.remove(supplier)
        self.transport_cost.pop(supplier.name)

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

    def isValid(self) -> bool:
        pass