from itertools import combinations
def subsets(nums):
    subset = [[]]
    for i in range(1, len(nums)+1):
        print(subset)
        subset += list(combinations(nums, i))


    return subset


print(subsets([1,2,3]))