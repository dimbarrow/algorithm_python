def plusOne(digits):
    digits_str = ''
    for i in range(len(digits)):
        digits_str += str(digits[i])

    digits_int = int(digits_str)+1
    digits_str = str(digits_int)
    new_dig = list()
    for i in range(len(digits_str)):
        new_dig.append(int(digits_str[i]))

    return new_dig


def plusOne2(digits):
    digits_str = ''
    for i in range(len(digits)):
        digits_str += str(digits[i])
    digits_int = int(digits_str) + 1
    digits_str = str(digits_int)
    if len(digits_str) == len(digits):
        for i in range(len(digits)):
            digits[i] = int(digits_str[i])
    else:
        for i in range(len(digits)):
            digits[i] = int(digits_str[i])
        new_l = len(digits_str)-len(digits)
        for i in range(new_l):
            digits.append(int(digits_str[digits[i+new_l]]))

    return digits