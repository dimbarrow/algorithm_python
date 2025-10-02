def removeElement(nums, val):
    counter = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[counter], nums[i] = nums[i], nums[counter]
            counter += 1

    return counter


print(removeElement([3,2,2,3], 3))