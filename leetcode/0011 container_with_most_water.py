def maxArea(height):
    left = 0
    right = len(height)-1
    V_max = []
    while left != right:
        V_max.append((height.index(height[right]) - height.index(height[left])) * min(height[left], height[right]))
        print(height.index(height[left]))
        print(height.index(height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right = right - 1

    return V_max


print(maxArea([1,8,6,2,5,4,8,3,7]))