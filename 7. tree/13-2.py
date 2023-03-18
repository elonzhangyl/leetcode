# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def binaryTreePaths(self, root):
        self.traverse(root)
        res_sorted = []
        for res in self.res:
            temp = ''.join([''.join(str(num)+'->') for num in res])
            res_sorted.append(temp[:-2])
        return res_sorted
    
    def traverse(self, node):
        if node:
            
            for i in [node.left, node.right]:
                self.path.append(node.val)
                self.traverse(i)
                if not node.left and not node.right:
                    self.res.append(self.path[:])
                self.path.pop()
            

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


print(Solution().binaryTreePaths(n1))