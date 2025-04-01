'''Given a binary tree, determine if it is  height-balanced.'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f'{self.val}'
    

def isBalanced(root: TreeNode) -> bool:

    if not root:
        return True

    def maxDepth(root: TreeNode) -> int:
        if root is None:
            return 0
        
        return 1 + max(maxDepth(root.left), maxDepth(root.right))
    
    left = maxDepth(root.left)
    right = maxDepth(root.right)

    if abs(left - right) > 1:
        return False
    
    return isBalanced(root.left) and isBalanced(root.right)


a = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(17)))
b = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
isBalanced(a)
