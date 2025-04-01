def two_sum(nums: list[int], target: int):
    hmap = dict()

    for i in range(len(nums)):
        if target - nums[i] in hmap:
            yield [nums[hmap[target - nums[i]]],nums[i]]
        hmap[nums[i]] = i


def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    used = set()

    for i in range(len(nums) - 2):
        ...

    return res


print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0, 1, 1]))
print(threeSum([0, 0, 0]))    
