def isPalindrome(x):
    x_l = str(x)

    print(x_l[:len(x_l) // 2])
    print(x_l[::-len(x_l) // 2])
    if x_l[:len(x_l)//2] == x_l[::-len(x_l)//2]:
        return True

    return False


print(isPalindrome(121))