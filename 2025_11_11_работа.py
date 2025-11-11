import sys
sys.setrecursionlimit(10**6)
def F(n):
    if n == 1:
        return 2
    elif n > 1 and F(n-1) < 7555444:
        return F(n-1)+6
    else:
        return F(n-1) - 7555444

print(F(100))
