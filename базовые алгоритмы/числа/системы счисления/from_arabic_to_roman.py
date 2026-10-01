def from_arabic_to_roman(num):
    M = ['', 'M', 'MM', 'MMM']
    C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'DM']
    X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    I = ['', 'I', 'II', 'III', 'IV', 'V', 'VII', 'VIII', 'IX']

    return M[num//1000]+C[(num%1000)//100]+X[(num%100)//10]+I[num%10]


print(from_arabic_to_roman(11))