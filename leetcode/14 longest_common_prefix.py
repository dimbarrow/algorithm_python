def longestCommonPrefix(strs):
    minimum = strs[0]
    for i in range(len(strs)-1):
        print(1)
        print(len(strs[i]))
        print(len(strs[i+1]))
        if len(strs[i]) < len(strs[i + 1]):
            minimum = strs[i]
        else:
            minimum = strs[i+1]
    print(minimum)

    new_strs = ""
    for i in range(len(minimum)):
        for g in range(len(strs)-1):
            if strs[g][i] != strs[i][i]:
                return new_strs
        new_strs += strs[i][i]

    return new_strs


print(longestCommonPrefix(["a"]))