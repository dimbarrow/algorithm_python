def isValid(s):
    if len(s) % 2 != 0:
        return False

    open = ['(', '{', '[']
    close = [')', '}', ']']
    a = '()'
    b = '{}'
    c = '[]'
    s_new = list()
    for i in range(len(s)):
        print(s_new)
        if s[i] in close:
            if len(s_new) == 0:
                return False
            if s[i] in c and s_new[-1] in c or s[i] in b and s_new[-1] in b or s[i] in a and s_new[-1] in a:
                s_new.remove(s_new[-1])
            else:
                return False
        else:
            s_new.append(s[i])

    return True

print(isValid("()[]{}"))