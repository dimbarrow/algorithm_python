def lengthOfLongestSubstring(s):
    substring = set()
    first = 0
    second = 0
    maxi = 0
    for i in range(len(s)):
        if s[first] not in substring:
            substring.add(s[first])
            first += 1
        else:
            maxi = max(maxi, len(substring))
            substring.remove(s[second])
            second += 1

    return maxi


print(lengthOfLongestSubstring("abcabcbb"))
