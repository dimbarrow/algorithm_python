lst = [int(i) for i in open("17.txt")]
counter = 0
sum_tr = 0
max_28 = -100000
for i in range(len(lst)):
    if str(lst[i])[-2:] == '28' and lst[i] > max_28:
        max_28 = lst[i]

for i in range(len(lst)-2):
    if len(str(lst[i])) == 3 or len(str(lst[i+1])) == 3 or len(str(lst[i+2])) == 3 and (lst[i] + lst[i+1] + lst[i+2]) / 3 > 0 and (lst[i] + lst[i+1] + lst[i+2]) / 3 < max_28:
        counter += 1
        if lst[i] + lst[i+1] + lst[i+2] > sum_tr:
            sum_tr = lst[i] + lst[i+1] + lst[i+2]

print(max_28)
print(counter)
print(sum_tr)