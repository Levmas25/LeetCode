'''Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f'{self.val}'

def sortedArrayToBST(nums: list[int]) -> TreeNode:
    
    if not nums:
        return None
    
    pos = len(nums) // 2
    root = TreeNode(nums[pos])

    root.left = sortedArrayToBST(nums[:pos])
    root.right = sortedArrayToBST(nums[pos + 1:])

    return root


nums = [-10, -3, 0, 5, 9]
sortedArrayToBST(nums)
    