def isHappy(n):
    nums = set()
    while n != 1:
            n = sum(int(x) ** 2 for x in str(n))
            print(n)
            if n not in nums:
                nums.add(n)
            else:
                return False

    return True

print(isHappy(2))