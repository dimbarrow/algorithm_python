def from_ten_to_two(num):
    lst = list()
    while num >= 2:
        lst.append(num%2)
        num //= 2
    lst.append(num)

    return lst[::-1]


print(from_ten_to_two(6))