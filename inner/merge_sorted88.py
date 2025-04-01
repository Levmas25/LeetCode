'''You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
 and the last n elements are set to 0 and should be ignored. nums2 has a length of n'''
def merge(nums1: list[list], n: int, nums2: list[int], m: int) -> None:
    i = n - 1
    j = m - 1

    while j >= 0:
        if nums2[j] >= nums1[i] or i < 0:
            nums1[i + j + 1] = nums2[j]
            j -= 1
        else:
            nums1[i + j + 1] = nums1[i]
            i -= 1

print(merge([1], 1, [], 0))