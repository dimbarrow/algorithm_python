import sys
sys.setrecursionlimit(10**6)

def F(n):
    if n <= 1:
        return 0
    elif n > 1 and n % 6 == 0:
        return n + F(n/6 - 2)
    elif n > 1 and n % 6 != 0:
        return n + F(n+6)



def from_19_to_ten():
    return int("11A93", 19) + int("123945", 19)

if from_19_to_ten() % 14 == 0:
        print(from_19_to_ten() / 14)

