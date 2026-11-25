'''инверсией считается ессли i<j
и lst[i]>lst[j]'''
lst = [1,2,3,5,4]
counter_inversion = 0
for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        counter_inversion += 1

print(counter_inversion)