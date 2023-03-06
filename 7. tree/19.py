
class Solution:
    def constructBinaryTree(self, order):
        if not order:
            return None

        root_val = max(order)
        root = TreeNode(root_val)


        idx = order.index(root_val)

        order_left = order[:idx]
        order_right = order[idx+1:]

        root.left = self.constructBinaryTree(order_left)
        root.right = self.constructBinaryTree(order_right)

        return root
                
class TreeNode: 
    def __init__(self, value=0):
        self.val = value
        self.left = None
        self.right = None

# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n6 = TreeNode(6)
# n7 = TreeNode(7)
# n8 = TreeNode(8)
# n9 = TreeNode(9)
# n1.left = n2
# n1.right = n3
# # n2.left = n4
# # n2.left = n5
# n3.left = n6
# n3.right = n7
# # n4.right = n8
# n6.right = n9

n1 = Solution().constructBinaryTree([3,2,1,6,0,5])
# s = Solution()
# s.hasPathSum(n1, 22)
# print(s.res)