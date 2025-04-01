'''Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.'''
def remove_elements(nums: list[int], val: int) -> int:
    to_place = len(nums) - 1
    i = 0

    while i < to_place:
        if nums[i] == val:
            nums[to_place], nums[i] = nums[i], nums[to_place]
            to_place -= 1
        else:
            i += 1

    if to_place == 0 and (not nums or nums[0] == val):
        nums.clear()
        return 0
    
    if nums[to_place] == val:
        return to_place 
    

    return len(nums) - (len(nums) - to_place - 1)

arr = [2, 2, 3, 3, 3]
print(remove_elements(arr, 3))
print(arr)


def from_solutions(nums: list[int], val: int) -> int:
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    
    return k