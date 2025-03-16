# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
def two_sum(nums: list[int], target: int) -> list[int]:
    hmap = dict()

    for i in range(len(nums)):
        if target - nums[i] in hmap:
            return [hmap[target - nums[i]], i]
        hmap[nums[i]] = i


print(two_sum([3, 3], 6))
