def isPalindrome(x):
    new_x = 0
    save_x = x
    while x > 0:
        new_x += x % 10
        x //= 10
        new_x *= 10

    new_x //= 10
    x = save_x

    return x == new_x


print(isPalindrome(121))