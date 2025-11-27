def isAnagram(s, t):
    s_set = set()
    t_set = set()
    for i in range(len(s)):
        s_set.add(s[i])

    for i in range(len(t)):
        t_set.add(t[i])

    if s_set == t_set:
        return True

    return False


print(isAnagram('rat', 'car'))
