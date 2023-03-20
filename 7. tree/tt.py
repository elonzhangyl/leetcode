class TreeNode: 
    def __init__(self, value=0):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res_l = []
        self.res_r = []

    def isSymmetric(self, root):
        if not root:
            return
        self.traversal_l(root.left)
        self.traversal_r(root.right)
        if self.res_l == self.res_r:
            return True
        return False
    
    def traversal_l(self, node):
        if node:
            self.res_l.append(node.val)
            self.traversal_l(node.left)
            self.traversal_l(node.right)
        else:
            self.res_l.append(None)
    
    def traversal_r(self, node):
        if node:
            self.res_r.append(node.val)
            self.traversal_r(node.right)
            self.traversal_r(node.left)
        else:
            self.res_r.append(None)

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(2)
n4 = TreeNode(3)
n5 = TreeNode(3)
n6 = TreeNode(6)
n7 = TreeNode(7)
n1.left = n2
n1.right = n3
n2.right = n4
n3.right = n5


print(Solution().isSymmetric(n1))