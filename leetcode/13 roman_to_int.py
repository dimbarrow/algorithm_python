def romanToInt(s):
    s_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s_nums_n = {'IV': 2, 'IX': 2, 'XL': 20, 'XC': 20, 'CD': 200, 'CM': 200}
    s_int = 0
    for i in range(len(s)):
        s_int += s_nums[s[i]]

    for i in range(len(s)-1):
        combine = s[i] + s[i+1]
        if combine in s_nums_n:
            s_int -= s_nums_n[combine]

    return s_int


print(romanToInt('XIX'))
