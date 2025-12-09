def canCompleteCircuit(gas, cost):
    gas_tr = 0
    index = 0
    for i in range(len(gas)):
        gas_tr += gas[i] - cost[i]
        if gas_tr < 0:
            gas_tr = 0
            index = i + 1
    if index < len(gas) and sum(gas) >= sum(cost):
        return index
    else:
        return -1