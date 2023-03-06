
class Solution:
    def combineBinaryTree(self, root1, root2):

        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
        elif not root1 and root2:
            root = TreeNode(root2.val)
        elif root1 and not root2:
            root = TreeNode(root1.val)
        elif not root1 and not root2:
            return None

        root.left = self.combineBinaryTree(root1.left, root2.left)
        root.right = self.combineBinaryTree(root1.right, root2.right)

        return root
                
class TreeNode: 
    def __init__(self, value=0):
        self.val = value
        self.left = None
        self.right = None

n11 = TreeNode(1)
n12 = TreeNode(2)
n13 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)
n21 = TreeNode(1)
n22 = TreeNode(2)
n23 = TreeNode(3)
n11.left = n12
n11.right = n13
n21.left = n22
n21.right = n23
# n12.left = n4
# n12.left = n5
# n13.left = n6
# n13.right = n7
# n4.right = n8
# n6.right = n9

print(Solution().combineBinaryTree(n11, n21))     
# s = Solution()
# s.hasPathSum(n1, 22)
# print(s.res)