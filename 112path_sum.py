'''Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path
such that adding up all the values along the path equals targetSum.'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: TreeNode, target: int) -> bool:

    if not root:
        return False

    queue = [(root, target)]
    while queue:
        node, s = queue.pop(0)

        if s - node.val == 0 and node != root and not (node.left or node.right): 
            return True
        
        if node.left:
            queue.append((node.left, s - node.val))
        if node.right:
            queue.append((node.right, s - node.val))

    return False





a = TreeNode(1, TreeNode(2), TreeNode(3))
b = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(1))))
c = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))
print(hasPathSum(c, 6))
