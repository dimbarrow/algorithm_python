def isPalindrome(s):
    if s == ' ':
        return True

    znaki = ",.:;'/@#"'_{[}\]"'
    new_str = list()
    for i in range(len(s)):
        if s[i] != ' ' and s[i] not in znaki:
            new_str.append(s[i].lower())

    if new_str[::-1] == new_str:
        return True

    print(new_str)
    print(new_str[::-1])
    return False


print(isPalindrome("Marge, let's \"[went].\" I await {news} telegram."))