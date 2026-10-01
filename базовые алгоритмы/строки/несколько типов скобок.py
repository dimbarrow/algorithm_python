#пишем через используя стек сверть инедксы списков
a = ['(', '{', '[']
b = [')', '}', ']']
s = input('Введите скобки:')
stack = []
def is_same_type(string, st):
    for i in range(len(string)):
        if string[i] in a:
            st.append(string[i])
        elif string[i] in b:
            if a.index(st[-1]) != b.index(string[i]):
                return False
            else:
                st.remove(st[-1])

    return True


print(is_same_type(s, stack))