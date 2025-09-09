def two_sum(nums, target):
    dict = {}
    dict[0] = nums[0]
    for i in range(len(nums)):
        if target - nums[i] not in dict:
            dict[i] = nums[i]
        else:
            return [dict[nums[i]], i]


print(two_sum([2,7,11,15], 9))