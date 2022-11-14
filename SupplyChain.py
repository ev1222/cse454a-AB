from Lane import Lane
from Customer import Customer
from Supplier import Supplier
from typing import List, Set

class SupplyChain():
    def __init__(self, name):
        self.name = name
        self.lanes: List[Lane] = []
        self.customers: Set[Customer] = [] # set because no repeats
        self.suppliers: Set[Supplier] = []

    def addLane(self, lane):
        self.lanes.append(lane)
        self.customers.append(lane.customer)
        self.suppliers.append(lane.supplier)

    def removeLane(self, lane):
        self.lanes.remove(lane)
        self.customers.remove(lane.customer)
        self.suppliers.remove(lane.supplier)

    def grossCost(self) -> float:
        gross_cost = 0
        for lane in self.lanes:
            gross_cost += lane.getLaneCost()
        return gross_cost
    
    def getLanes(self) -> list:
        return self.lanes
        

    #TODO: add addt'l checks for other constraints
    def isValid(self) -> bool:
        flag = True
        # for every customer, check the supplier capacity in each lane with that customer
        # if the total supplier capacity is less than the customer demand, not valid
        for customer in self.customers:
            demand = customer.demand
            capacity = 0
            for lane in self.lanes:
                if customer is lane.customer:
                    capacity += lane.supplier.capacity
            if capacity < demand:
                print(f'{customer.name} demand is not met') # for debugging purposes
                flag = False
        return flag
