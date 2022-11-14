import csv
from SupplyChain import SupplyChain

def generateCSV(sc: SupplyChain) -> tuple[bool, str]:
    lanes = sc.getLanes()

    header = ['Lane Name', 'Product', 'Customer Name', 'Supplier Name', 'Transport Cost', 'Lane Cost']
    data = []

    for lane in lanes:
        lane_name = lane.name
        lane_product_name = lane.customer.product.name
        lane_customer = lane.customer
        lane_supplier = lane.supplier
        lane_transport_cost = lane.transport_cost
        lane_cost = lane.getLaneCost()
        data.append([lane_name, lane_product_name, lane_customer.name, lane_supplier.name, lane_transport_cost, lane_cost])

    data.append([])
    data.append(['Total cost of supply chain:'])
    data.append([sc.grossCost()])

    try:
        with open('supply_chain_overview.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
        return (True, 'success')
    except csv.Error as e:
        return (False, e)
    


    


    