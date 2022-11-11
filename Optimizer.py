from Customer import Customer
from Supplier import Supplier
from Lane import Lane
from SupplyChain import SupplyChain
from typing import List, Set

def optimize(lanes: List[Lane]) -> SupplyChain:
    #check for valid input
    if not lanes:
        print("Invalid input")

    sc = SupplyChain("sc")

    # populate customers from list of lanes 
    customers: List[Customer] = [lane.customer for lane in lanes]

    # sort customers by demand in descending order
    customers.sort(key=lambda x: x.demand, reverse=True)
 
    # lanes.sort(key=lambda x: x.supplier.capacity, reverse=True)

    # take customer with highest demand
    for customer in customers:
        demand = customer.demand
        capacity = 0
        # create list of contextual lanes sorted by their capcity in decreasing order
        context_lanes = [lane for lane in lanes if lane.customer == customer]
        context_lanes = sorted(context_lanes, key=get_key)
        
        # add highest capacity supplier for that customer -- greedy!                
        for lane in context_lanes:
            sc.addLane(lane)
            capacity += lane.supplier.capacity
            # remove lane from lists to avoid double counting 
            context_lanes.remove(lane)
            lanes.remove(lane)
            # if demand is met, stop adding lanes for that customer
            if capacity >= demand:
                break
    
    if not sc.isValid():
        print("Something went terribly wrong") # debugging purposes              

    return sc

def get_key(lane):
    return (-1*lane.supplier.capacity, lane.transport_cost)