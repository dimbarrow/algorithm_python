def reverseVowels(s):
    vowels = 'AEIOUaeiou'
    vowels_in_s = []
    for i in range(len(s)):
        print(s[i])
        if s[i] in vowels:
            print(1)
            vowels_in_s.append(s[i])

    return vowels_in_s


print(reverseVowels(["IceCreAm"]))