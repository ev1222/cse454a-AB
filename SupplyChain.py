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

    def grossCost(self) -> float:
        gross_cost = 0
        for lane in self.lanes:
            gross_cost += lane.getLaneCost()
        return gross_cost

    #TODO: add addt'l checks for other constraints
    def isValid(self) -> bool:
        flag = True
        for lane in self.lanes:
            if not lane.isValid():
                flag = False
                print(f'{lane.name} is not valid') # for debugging purposes
        return flag
