# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def sumOfLeftLeaves(self, root) -> int:
        self.traverse(root)
        return self.res

    def traverse(self, node):
        if node:
            if node.left and not node.left.left and not node.left.right:
                self.res += node.left.val
            self.traverse(node.left)
            self.traverse(node.right)


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n1.left = n2
n1.right = n3
n3.left = n6
n3.right = n7
print(Solution().sumOfLeftLeaves(n1))     
