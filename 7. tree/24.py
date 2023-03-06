
class Solution:
    def minBST(self, root):
        res = []

        def inorderTraversal(root):
            if not root:
                return
            inorderTraversal(root.left)
            res.append(root.val)
            inorderTraversal(root.right)

        inorderTraversal(root)
        for i in range(len(res)-1): # 有序数组求最小值
            r = min(res[i+1]-res[i], r)
        return r
                
class TreeNode: 
    def __init__(self, value=0):
        self.val = value
        self.left = None
        self.right = None

n1 = TreeNode(5)
n2 = TreeNode(1)
n3 = TreeNode(4)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
n6 = TreeNode(3)
n7 = TreeNode(6)
# n8 = TreeNode(8)
# n9 = TreeNode(9)
n1.left = n2
n1.right = n3
# # n2.left = n4
# # n2.left = n5
n3.left = n6
n3.right = n7
# # n4.right = n8
# n6.right = n9

n1 = Solution().isBinarySearchTree(n1)
# s = Solution()
# s.hasPathSum(n1, 22)
# print(s.res)