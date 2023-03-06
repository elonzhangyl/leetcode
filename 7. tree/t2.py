from collections import deque

class TreeNode: 
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left #中
        self.invertTree(root.left) #左
        self.invertTree(root.right) #右
        return root

n1 = None

aa = Solution().invertTree(n1)