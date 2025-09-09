def two_sum(nums, target):
    dict = {}
    dict[nums[0]] = 0
    for i in range(len(nums)):
        if target - nums[i] not in dict:
            dict[nums[i]] = i
        else:
            return [dict[target - nums[i]], i]


print(two_sum([2,7,11,15], 9))