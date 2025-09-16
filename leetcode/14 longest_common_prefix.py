def longestCommonPrefix(strs):
        st = set()

        for i in range(len(strs)):
            st.add(strs[i][0])
        if len(st) != 1:
            return False

        st = set()
        minim = strs[0]
        for i in range(len(strs)):
            if strs[0] > strs[i]:
                minim = strs[i]

        counter = 0
        for i in range(len(strs)):
            for g in range(len(minim)):
                st.add(strs[g][i])
            if len(st) == i:
                counter += 1
            else:
                return strs[0][counter]


print(longestCommonPrefix(["flower","flow","flight"]))