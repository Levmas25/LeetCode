'''Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    
    if p is None and q is None:
        return True
    
    if p is None or q is None:
        return False

    return isSameTree(p.left, q.left) and (p.val == q.val) and isSameTree(p.right, q.right)



p = TreeNode(2, right=TreeNode(3))
q = TreeNode(2, right=TreeNode(3))
print(isSameTree(p, q))