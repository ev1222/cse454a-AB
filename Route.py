from Lane import Lane
from Customer import Customer
from typing import List

class Route():
    def __init__(self, name, customer: Customer):
        self.name = name
        self.lanes: List[Lane] = []
        self.customer = customer

    def addLane(self, lane):
        self.lanes.append(lane)

    def removeLane(self, lane):
        self.lanes.remove(lane)

    def grossCost(self) -> float:
        gross_cost = 0
        for lane in self.lanes:
            gross_cost += lane.getLaneCost()
        return gross_cost

    #TODO: add addt'l checks for other constraints
    def isValid(self) -> bool:
        capacity = 0
        for lane in self.lanes:
            capacity += lane.supplier.capacity
        if capacity < self.customer.demand:
            print(f'{self.name} is not valid') # for debugging purposes
            return False
        return True
