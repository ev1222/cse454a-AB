from Customer import Customer
from Supplier import Supplier

#TODO: if need be, implement more granular calculations of transport cost
class Lane(): 
    def __init__(self, name, customer: Customer, supplier: Supplier, transport_cost):
        self.name = name
        self.customer = customer
        self.supplier = supplier
        self.transport_cost = transport_cost # per 100 lbs, hardcoded for now

    def getGrossShippingCost(self) -> float:
        total_prod_weight = self.supplier.capacity * self.supplier.product.weight
        gross_shipping_cost = total_prod_weight/100 * self.transport_cost
        return gross_shipping_cost

    def getGrossProductionCost(self) -> float:
        gross_production_cost = self.supplier.total_prod_cost
        return gross_production_cost
    
    def getLaneCost(self) -> float:
        return self.getGrossProductionCost() + self.getGrossShippingCost()