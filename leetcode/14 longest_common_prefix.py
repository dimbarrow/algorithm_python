def longestCommonPrefix(strs):
    minimum = strs[0]
    ind_min = 0
    for i in range(len(strs)-1):
        if len(strs[i]) < len(strs[i + 1]):
            minimum = strs[i]
            ind_min = i
        else:
            minimum = strs[i+1]
            ind_min = i
    print(minimum)

    new_strs = ""
    for i in range(len(minimum)):
        for k in range(len(strs)):
            if strs[k][i] != strs[ind_min][i]:
                return new_strs
        new_strs += strs[ind_min][i]

    return new_strs


print(longestCommonPrefix(["caa","","a","acb"]))