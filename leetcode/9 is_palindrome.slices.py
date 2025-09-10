def isPalindrome(x):
    x_l = str(x)

    if x_l[:len(x_l)] == x_l[:-len(x_l)]:
        return True

    return False

