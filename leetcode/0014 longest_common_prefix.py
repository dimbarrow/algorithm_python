def longestCommonPrefix(strs):
    minimum = strs[0]
    ind_min = 0
    for i in range(1, len(strs)):
        if minimum > strs[i]:
            minimum = strs[i]
    print(minimum)

    new_strs = ""
    for i in range(len(minimum)):
        for k in range(len(strs)):
            if strs[k][i] != strs[i][i]:
                return new_strs
        new_strs += strs[ind_min][i]

    return new_strs


print(longestCommonPrefix(["caa","","a","acb"]))