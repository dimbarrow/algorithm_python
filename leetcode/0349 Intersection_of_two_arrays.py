def intersection(nums1, nums2):
    st = set()
    for i in range(min(len(nums1),len(nums2))):
        if len(nums1) < len(nums2):
            if nums1[i] in nums2:
                st.add(nums1[i])
        else:
            if nums2[i] in nums1:
                st.add(nums2[i])

    return list(st)

print(intersection([1,2,2,1], [2,2]))