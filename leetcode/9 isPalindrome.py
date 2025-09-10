def isPalindrome(x):
    x_l = str(x)

    if x_l[:len(x_l)] == x_l[::-1]:
        return True

    return False


print(isPalindrome(121))