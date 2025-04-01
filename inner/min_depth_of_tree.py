'''Given a binary tree, find its minimum depth.'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f'{self.val}'

def minDepth(root: TreeNode) -> int:
    '''Beats only 11% of solutions. Has bad memo as well❌❌❌❌❌'''
    if root is None:
        return 0
    
    left = minDepth(root.left)
    right = minDepth(root.right)

    if root.left is None and root.right:
        left = 10**10

    if root.right is None and root.left:
        right = 10**10
        
    return 1 + min(left, right)


def solution(root: TreeNode) -> int:
    '''100% speed, also good memo✅✅✅✅✅'''
    if not root:
        return 0
    
    # Initialize the queue with the root node and its depth
    queue = [(root, 1)]
    
    while queue:
        # Dequeue the first node and its depth
        node, depth = queue.pop(0)
        
        # If the node is a leaf, return its depth
        if not node.left and not node.right:
            return depth
        
        # Enqueue the left and right children if they exist
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))


a = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
minDepth(a)