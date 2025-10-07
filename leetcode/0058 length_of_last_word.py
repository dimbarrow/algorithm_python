def lengthOfLastWord(s):
    lst = []
    counter = 0
    if ' ' not in s:
        return len(s)

    for i in range(len(s)):
        if s[i] != ' ':
            counter += 1
            print(counter)
        elif s[i] == ' ':
            lst.append(counter)
            counter = 0

    lst.append(counter)


    for i in range(len(lst), 0, -1):
        if lst[i-1] != 0:
            return lst[i-1]

    return lst[len(lst)-1]