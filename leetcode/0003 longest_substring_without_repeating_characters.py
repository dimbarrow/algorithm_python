def lengthOfLongestSubstring(s):
    substring = set()
    first = 0
    second = 0
    maxi = 0
    if s == " ":
        return 1
    while first != len(s):
        if s[first] not in substring:
            substring.add(s[first])
            first += 1
            print('байден')
            print(substring)
        else:
            maxi = max(maxi, len(substring))
            print('обама')
            print(maxi)
            substring.remove(s[second])
            second += 1
            print('трамп')
            print(substring)

    return maxi


print(lengthOfLongestSubstring("pwwkew"))
