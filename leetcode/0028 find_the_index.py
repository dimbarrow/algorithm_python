def strStr(haystack, needle):
    if haystack == needle:
        return 0
    for i in range(len(haystack) - 1):
        if needle == haystack[i:i + len(needle)]:
            return i
    if haystack[len(haystack) - 1] == needle:
        return len(haystack) - 1
    return -1