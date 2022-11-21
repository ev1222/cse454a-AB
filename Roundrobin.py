###### Pseudocode

# Given a list of lanes, sort by cheapest supplier production cost,
# and take percentage of that capacity for each customer round-robin style,
# removing old lane from list and adding a new lane with x% less capacity.

# Take a brewery 20% of demand

# Optimize by production cost

customer:brewery

optimize(lanes, percentage):
	sorted_lanes = sort lanes by cheapest supplier production cost
	sc = SupplyChain()

	while sorted_lanes is not empty:
		lane = lane popped from sorted_lanes		

		for each customer in customers:
			curr_customer = sorted_custmor.pop(customer)
			ingredient_used = percentage * initial_demand[curr_customer]
			remainder = max(capacity_remainder or curr_customer.demand)			
			lane.capacity -= ingredient_used or remainder;
			curr_customer.demand -= ingredient_used or remainder;
			sorted_customers.add(curr_customer)
			
			if curr_customer.demand < 0: continue

			if lane.capacity < 0:
					Remove lane from sorted_lanes
					Add lane to sc
					break

		return sc				
			
			
			
