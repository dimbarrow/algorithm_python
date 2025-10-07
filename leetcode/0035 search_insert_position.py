def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] - target == 0:
            return i

    if target > nums[len(nums) - 1]:
        return i + 1

    for i in range(len(nums)):
        if target < nums[i]:
            return i