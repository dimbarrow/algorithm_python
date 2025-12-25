def minCostClimbingStairs(cost):
    lst = list()
    for i in range(1, len(cost),2):
        print(i)
        print(min(cost[i-1], cost[i-2]), 'a')
        print(cost[i-1], cost[i-2], 'b')
        lst.append(min(cost[i-1], cost[i-2]))

    return sum(lst)


print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))