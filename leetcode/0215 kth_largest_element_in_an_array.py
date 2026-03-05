def findKthLargest(nums, k):
    minimum = min(nums)
    ch_lst = [0] * (max(nums) - minimum + 1)
    for i in range(len(nums)):
        ch_lst[nums[i] - minimum] += 1

    counter = len(ch_lst) - 1
    while k > 0:
        k -= ch_lst[counter]
        counter -= 1

    return counter + minimum + 1

print(findKthLargest(nums = [3,2,1,5,6,4,10], k = 2))
