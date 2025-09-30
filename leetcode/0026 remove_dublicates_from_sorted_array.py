from distutils.fancy_getopt import fancy_getopt


def removeDuplicates(nums):
    check_nums = []
    counter = 0
    for i in range(len(nums)):
        if nums[i] in check_nums:
            counter += 1
        else:
            check_nums.append(nums[i])

    k = len(check_nums)
    for i in range(counter):
        check_nums.append('_')

    for i in range(len(nums)):
        nums[i] = check_nums[i]


    return k


def removeDuplicates2(nums):
    k = 0
    g = 0
    while g != len(nums):
        if nums[k] != nums[g]:
            k += 1
            nums[k] = nums[g]
        g+=1

    return nums, k


print(removeDuplicates2([1,1,2]))