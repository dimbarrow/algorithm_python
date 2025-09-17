def longestCommonPrefix(strs):
    st = set()


    if strs == [""]:
        return ""

    for i in range(len(strs)):
        if strs[i] == "":
            return ""

    for i in range(len(strs)):
        st.add(strs[i][0])

    if len(st) != 1:
        return ""

    st = set()
    minim = strs[0]
    for i in range(len(strs)-1):
        if len(strs[i]) > len(strs[i+1]):
            minim = strs[i+1]

    maxim = 0
    for i in range(len(strs)-1):
        if len(strs[i]) < len(strs[i + 1]):
            maxim = i+1

    counter = 0
    for i in range(len(minim)):
        for g in range(len(strs)):
            st.add(strs[g][i])
            print(st)
        if len(st) == i + 1:
            counter += 1
        elif len(st) != i + 1:
            return strs[maxim][:counter]
        else:
            return strs[0]

    return strs[maxim][:counter]


print(longestCommonPrefix(["a","a","a"]))