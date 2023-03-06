
class Solution:
    def binarySearchTree(self, root, target):
        if not root:
            return None

        if root.val == target:
            return root
        elif root.val < target:
            return self.binarySearchTree(root.right, target)
        else:
            return self.binarySearchTree(root.left, target)
                
class TreeNode: 
    def __init__(self, value=0):
        self.val = value
        self.left = None
        self.right = None

n1 = TreeNode(2)
n2 = TreeNode(1)
n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n6 = TreeNode(6)
# n7 = TreeNode(7)
# n8 = TreeNode(8)
# n9 = TreeNode(9)
n1.left = n2
n1.right = n3
# # n2.left = n4
# # n2.left = n5
# n3.left = n6
# n3.right = n7
# # n4.right = n8
# n6.right = n9

n1 = Solution().binarySearchTree(n1, 3)
# s = Solution()
# s.hasPathSum(n1, 22)
# print(s.res)