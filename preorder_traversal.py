'''Given the root of a binary tree, return the preorder traversal of its nodes' values.'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: TreeNode) -> list[int]:

    def inner(node: TreeNode):
        if not node:
            return  
        yield node.val
        yield from inner(node.left)
        yield from inner(node.right)
    
    return list(inner(root))
    


tree1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))), TreeNode(3, TreeNode(8, TreeNode(9))))
tree2 = TreeNode(1, right=TreeNode(2, TreeNode(3)))
print(preorder_traversal(tree2))