'''Given the root of a binary tree, return the postorder traversal of its nodes' values.'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root: TreeNode) -> list[int]:

    res = []

    def inner(node: TreeNode):
        if node:
            inner(node.left)
            inner(node.right)
            res.append(node.val)

    inner(root)
    return res

tree1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))), TreeNode(3, TreeNode(8, TreeNode(9))))
tree2 = TreeNode(1, right=TreeNode(2, TreeNode(3)))
print('\n', postorderTraversal(tree1))
print('\n', postorderTraversal(tree2))
print('\n', postorderTraversal(None))