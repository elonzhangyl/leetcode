class Solution:
    def rob(self, root):
        self.traverse(root)
        return
    def traverse(self, node):
        if not node:
            return [0 , 0]
        dp_left = self.traverse(node.left)
        dp_right = self.traverse(node.right)
        dp = [0, 0]
        # 不考虑偷当前node，考虑偷其子节点
        dp[0] = max(dp_left[0], dp_left[1]) + max(dp_right[0], dp_right[1])
        # 考虑偷当前node，不考虑偷其子节点
        dp[1] = node.val + dp_left[0] + dp_right[0]
        return dp

class TreeNode: 
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None
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
    print(Solution().rob(n1))
    # print(Solution().inorderTraversal(node1))
    # print(Solution().postorderTraversal(node1))
    # print(Solution().preorderTraversal(node0))
    # print(Solution().preorderTraversal(node11))


