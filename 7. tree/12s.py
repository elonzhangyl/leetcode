# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.get_height(root) != -1:
            return True
        else:
            return False
    
    def get_height(self, node: TreeNode) -> int:
        if not node:
            return 0
        h_left = self.backtrack(node.left)
        h_right = self.backtrack(node.right)
        if abs(h_left - h_right) > 1:
            return -1
        if h_left == -1:
            return -1
        if h_right == -1:
            return -1
        return max(h_left, h_right) + 1
        

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n1.left = n2
n1.right = n3
# n2.left = n5
# n2.right = n4
# n3.left = n7
# n3.right = n6
print(Solution().isBalanced(n1))