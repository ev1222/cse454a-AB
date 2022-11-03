from dataclasses import dataclass
from Customer import Customer
from Supplier import Supplier

#TODO: if need be, implement more granular calculations of transport cost
@dataclass
class Lane(): 
    supplier: Supplier
    customer: Customer
    #transport_cost: float #per 100 lbs

    #TODO: eventually make this able to lookup from dataset transport cost
    def get_transport_cost(self) -> float:
        self.transport_cost = 6.95

    def get_gross_shipping_cost(self) -> float:
        total_prod_weight = self.supplier.capacity * self.supplier.product.weight 
        transport_cost = self.get_transport_cost()
        gross_shipping_cost = total_prod_weight/100 * transport_cost
        return gross_shipping_cost
    