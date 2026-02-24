def calculate(s):
    znak = '+-*/ '
    current_number = 0
    previous_operator = '+'
    stack = []

    for index, char in enumerate(s):
        print(stack)
        if char not in znak:
            current_number = current_number * 10 + int(char)
        if index == len(s)-1 or char in znak:
            if previous_operator == '+':
                stack.append(current_number)
            elif previous_operator == '-':
                stack.append(-current_number)
            elif previous_operator == '*':
                stack.append(stack.pop() * current_number)
            elif previous_operator == '/':
                stack.append(int(stack.pop() / current_number))

            previous_operator = char
            current_number = 0


    return sum(stack)

print(calculate("3/2+2*2-1+3/3"))