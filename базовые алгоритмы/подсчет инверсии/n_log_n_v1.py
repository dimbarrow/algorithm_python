def count_inversions(lt, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2

    inversions = count_inversions(lt, left, mid)
    inversions += count_inversions(lt, mid + 1, right)

    merged = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if lt[i] <= lt[j]:
            merged.append(lt[i])
            i += 1
        else:
            merged.append(lt[j])
            inversions += mid - i + 1
            j += 1

    while i <= mid:
        merged.append(lt[i])
        i += 1

    while j <= right:
        merged.append(lt[j])
        j += 1

    for k in range(len(merged)):
        lt[left + k] = merged[k]

    return inversions


nums = list((4, 3, 2, 1))
print(count_inversions(nums,0, len(nums) - 1))
