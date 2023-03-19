from collections import deque

class TreeNode: 
    def __init__(self, value=0):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def breadthFirstTraverse(self, root:TreeNode) -> list[int]:
        level = deque([root])
        res = []
        while level:
            dd = []
            for _ in range(len(level)):
                node = level.popleft()
                dd.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            res.append(dd)
        return res



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

print(Solution().breadthFirstTraverse(n1))