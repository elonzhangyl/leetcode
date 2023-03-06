from collections import deque


class Solution:
    def leftLeaf(self, root):
        que = deque([root])
        res = 0
        while que:
            for _ in range(len(que)):
                cur = que.popleft()
                if cur.left:
                    que.append(cur.left)
                    if cur.left.left is None and cur.left.right is None:
                        res = cur.left.val
                if cur.right:
                    que.append(cur.right)
        return res
                
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


print(Solution().leftLeaf(n1))     
# s = Solution()
# s.leftLeafSum(n1)
# print(s.res)