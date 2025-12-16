from itertools import combinations
def subsets(nums):
    subset = list()
    for i in range(len(nums)+1):
        subset.append(list(combinations(nums, i)))

    return subset


print(subsets([1,2,3]))