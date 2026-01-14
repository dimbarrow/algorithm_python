def getLongestSubsequence(words, groups):
    if len(words) <= 1:
        return words

    lst = list()
    for i in range(len(words)-1):
        if groups[i] != groups[i+1]:
            lst.append(words.index(words[i]))
            lst.append(words.index(words[i+1]))

    print(lst)
    st = set()
    for i in range(len(lst)):
        st.add(lst[i])
    st = list(st)
    return_lst = list()
    for i in range(len(st)):
        return_lst.append(words[st[i]])

    if len(return_lst) == 0:
        return [words[0]]

    return return_lst