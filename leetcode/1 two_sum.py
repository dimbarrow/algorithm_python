def two_sum(nums, target):
    d_dict = {}
    for i in range(len(nums)):
        if target - nums[i] in d_dict:
            return [d_dict[target - nums[i]], i]
        d_dict[nums[i]] = i

    return None

print(two_sum([2,7,11,15], 9))