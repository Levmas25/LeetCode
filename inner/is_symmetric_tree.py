'''Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'
    
def isSymmetric(root: TreeNode) -> bool:
    
    return isMirror(root.left, root.right) 
    


def isMirror(p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
        return True
    
    if p is None or q is None:
        return False

    return isSymmetric(p.left, q.right) and (p.val == q.val) and isSymmetric(p.right, q.left)



p = TreeNode(2, right=TreeNode(3))
q = TreeNode(2, right=TreeNode(3))
print(isSymmetric(p, q))