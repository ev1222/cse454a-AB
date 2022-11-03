from Lane import Lane
from typing import List

class SupplyChain():
    def __init__(self, name):
        self.name = name
        self.lanes: List[Lane] = []

    def addLane(self, lane):
        self.lanes.append(lane)

    def removeLane(self, lane):
        self.lanes.remove(lane)

    def grossCost(self):
        gross_cost = 0
        for lane in self.lanes:
            gross_cost += lane.getLaneCost()
        return gross_cost