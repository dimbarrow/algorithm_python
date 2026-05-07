def letterCombinations(digits):
    nums = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    results = []

    def rec(index, cur_string):
        if len(cur_string) == len(digits):
            results.append(cur_string)
            return

        letters = nums[digits[index]]
        for i in letters:
            rec(index + 1, cur_string + i)

    rec(0, "")
    return results

print(letterCombinations('23456789'))


def letterCombinationsTwo(digits):
    if not len(digits):
        return ""

    for i in range(len(digits)):


    comb = []
    for prefix in prefixs:
        for digit in digits:
            comb.append(prefix+digit)
