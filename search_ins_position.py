'''Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.'''
def search_insert(nums: list[int], target: int) -> int:
    r = 0
    l = len(nums) - 1
    prev_mid = 0

    if target > nums[-1]:
        return len(nums)
    
    if target < nums[0]:
        return 0

    while r <= l:
        mid = (r + l) // 2
            
        if nums[mid] > target:
            l = mid
        elif nums[mid] < target:
            r = mid
        else:
            return mid
        
        if l == r + 1 and prev_mid == mid:
            return l

        prev_mid = mid
        
    return len(nums)
        
    
print(search_insert([1, 3, 5], 1))


def how_should_be(nums: list[int], target: int) -> int:
    '''Bibos nepravilno napisal dvoichny poisk❌❌❌❌❌'''
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return left
