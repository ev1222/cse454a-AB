from Customer import Customer
from Supplier import Supplier
from Lane import Lane
from SupplyChain import SupplyChain
from typing import List, Set

def optimize(lanes: List[Lane]) -> SupplyChain:
    sc = SupplyChain("sc")

    # populate customers from list of lanes argument
    for lane in lanes:
        customers: List[Customer] = [].append(lane.customer)

    # sort customers by demand in descending order
    customers.sort(key=lambda x: x.demand, reverse=True) 

    # take customer with highest demand
    for customer in customers:
        demand = customer.demand
        capacity = 0
        for lane in lanes:
            if lane.customer is customer:
                sc.addLane(lane)
                capacity += lane.supplier.capacity
                # lane no longer available for use
                lanes.remove(lane)
                # if demand is met, stop adding lanes for that customer
                if capacity >= demand:
                    break
    
    if not sc.isValid():
        print("Something went terribly wrong") # debugging purposes              

    return sc