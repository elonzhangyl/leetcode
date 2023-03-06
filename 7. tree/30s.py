class Solution:

    def deleteBST(self, root, p):
        if not root:
            return root

        if root.val > p:
            root.left = self.deleteBST(root.left, p)
        elif root.val < p:
            root.right = self.deleteBST(root.right, p)
        else:
            # 左空右空
            if not root.left and not root.right:
                return None
            if root.left and not root.right:
                return root.left
            if not root.left and root.right:
                return root.right
            if root.left and root.right:
                node = root.right
                while node.left:
                    node = node.left
                node.left = root.left
                root = root.right
                return root

        


class TreeNode: 
    def __init__(self, value=0):
        self.val = value
        self.left = None
        self.right = None

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
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

n1 = Solution().insertBST(n1,TreeNode(6.5))
# s = Solution()
# s.hasPathSum(n1, 22)
# print(s.res)