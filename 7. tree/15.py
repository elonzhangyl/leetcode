class Solution:
    def __init__(self) -> None:
        self.res = 0

    def leftLeafSum(self, root):
        if root.left:
            if root.left.left is None and root.left.right is None:
                self.res += root.left.val
            self.leftLeafSum(root.left)
        if root.right:
            self.leftLeafSum(root.right)


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
n1.left = n2
n1.right = n3
n3.left = n6
n3.right = n7


print(Solution().leftLeafSum(n1))     
s = Solution()
s.leftLeafSum(n1)
print(s.res)