nums = [int(i) for i in open('17.txt')]

max_28 = 0
for i in range(len(nums)):
    if str(nums[i])[-2:] == '28' and nums[i] > max_28:
        max_28 = nums[i]

count = 0
max_sum = -10 ** 9

for i in range(len(nums) - 2):
    a, b, c = nums[i], nums[i + 1], nums[i + 2]

    if not (100 <= abs(a) <= 999 or 100 <= abs(b) <= 999 or 100 <= abs(c) <= 999):
        continue

    s = a + b + c
    if s <= 0:
        continue

    if s >= 3 * max_28:
        continue

    count += 1
    if s > max_sum:
        max_sum = s

print(count)
print(max_sum)
