def isIsomorphic(s, t):
    l1 = [0] * 256
    l2 = [0] * 256
    for i in range(len(s)):
        if l1[ord(s[i])] == l2[ord(t[i])]:
            l1[ord(s[i])] = i + 1
            l2[ord(t[i])] = i + 1
        else:
            return False

    return True


print(isIsomorphic("badc", "baba"))