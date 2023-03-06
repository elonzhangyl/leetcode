class TreeNode: 
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root):
        self.res.append(root.value)
        if root.left:
            self.preorderTraversal(root.left)
        if root.right:
            self.preorderTraversal(root.right)

    def inorderTraversal(self, root):
        if root.left:
            self.preorderTraversal(root.left)
        self.res.append(root.value)
        if root.right:
            self.preorderTraversal(root.right)

# driver code
if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n1.left = n3
    n1.right = n2
    n2.left = n5
    n2.right = n4
    n3.left = n7
    n3.right = n6
    s = Solution()
    s.preorderTraversal(n1)
    s.res
    print(Solution().preorderTraversal(n1))
    # print(Solution().inorderTraversal(node1))
    # print(Solution().postorderTraversal(node1))
    # print(Solution().preorderTraversal(node0))
    # print(Solution().preorderTraversal(node11))