'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such 
that each unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.'''
def remove_dublicates(nums: list[int]) -> int:
    unique = {nums[0]}
    to_place = 1

    for i in range(1, len(nums)):
        if nums[i] not in unique:
            nums[to_place] = nums[i]
            unique.add(nums[i])
            to_place += 1
    
    return len(unique)
        


nums = [1, 1, 2, 2, 4]
print(remove_dublicates(nums))
print(nums)