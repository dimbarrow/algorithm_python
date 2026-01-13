from pkgutil import walk_packages


def getLongestSubsequence(words, groups):
    lst = list()
    for i in range(len(groups)-1):
        if groups[i] != groups[i+1]:
            lst.append(i)

    counter = 0
    print(lst)
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1] and lst[i+1]-lst[i] == 1:
            counter += 1
        else:
            break

    return words[:counter]

print(getLongestSubsequence(["a","b","c","d"], [1,0,1,1]))