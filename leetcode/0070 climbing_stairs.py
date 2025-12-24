def climbStairs(n):
    if n <= 2:
        return n
    st = [0] * n
    st[0] = 1
    st[1] = 2
    for i in range(2, n):
        st[i] = st[i - 1] + st[i - 2]

    return st[-1]

print(climbStairs(6))

def climbingStairs_noLists(n):
    if n <= 2:
        return n
    first = 1
    second = 1
    local = 0
    for i in range(n):
        local = first
        first = first+second
        second = local

    return local

print(climbingStairs_noLists(6))