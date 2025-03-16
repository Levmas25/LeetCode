'''Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f'{self.val}'


def maxDepth(root: TreeNode) -> int:
    if root is None:
        return 0
        
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


a = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
b = TreeNode(1, TreeNode(2))
print(maxDepth(b))