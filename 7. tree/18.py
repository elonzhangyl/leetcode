
class Solution:
    def constructBinaryTree(self, inorder, postorder):
        if not postorder: 
            return None

        root = TreeNode(postorder[-1])

        idx = inorder.index(postorder[-1])

        inorder_left = inorder[:idx]
        inorder_right = inorder[idx+1:]
        postorder_left = postorder[:idx]
        postorder_right = postorder[idx:-1]

        root.left = self.constructBinaryTree(inorder_left, postorder_left)
        root.right = self.constructBinaryTree(inorder_right, postorder_right)

        return root
                
class TreeNode: 
    def __init__(self, value=0):
        self.val = value
        self.left = None
        self.right = None

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)
n1.left = n2
n1.right = n3
# n2.left = n4
# n2.left = n5
n3.left = n6
n3.right = n7
# n4.right = n8
# n6.right = n9

print(Solution().constructBinaryTree([2,1,6,3,7], [2,6,7,3,1]))     
# s = Solution()
# s.hasPathSum(n1, 22)
# print(s.res)