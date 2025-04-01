# M3O-232Б-23
# Минасян 

def maxArea(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    area = 0

    while left < right:

        area = max(area, min(height[left], height[right])*(right-left))

        if height[right] > height[left]:
            left += 1
            continue

        if height[left] >= height[right]:
            right -= 1

    return area


print('\n')
print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1, 1]))
print(maxArea([1,2,4,3]))
