roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
roman_comb = {'IV': 2, 'IX': 2, 'XL': 20, 'XC': 20, 'CD': 200, 'CM': 200}
def from_roman_to_arabic(r_numb, r_d, r_c):
    arabic_num = 0
    for i in range(len(r_numb)):
        if r_numb[i] in r_d:
            arabic_num += r_d[r_numb[i]]

    for i in range(len(str(arabic_num))):
        if r_numb[i:i+2] in r_c:
            arabic_num -= r_c[r_numb[i:i+2]]

    return arabic_num


print(from_roman_to_arabic('XXXV', roman_dict, roman_comb))
