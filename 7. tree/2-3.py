# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.c = 0

    def countNodes(self, root: TreeNode) -> int:
        return self.getNodesNum(root)
        
    def getNodesNum(self, cur):
        if not cur:
            return 0
        for child in [cur.left, cur.right]:
            c = self.getNodesNum(child) #左
            self.c += c
        return self.c + 1


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
print(Solution().countNodes(n1))