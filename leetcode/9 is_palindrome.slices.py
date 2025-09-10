def isPalindrome(x):
    x_l = str(x)

    return x_l[:len(x_l)] == x_l[:-len(x_l)]

