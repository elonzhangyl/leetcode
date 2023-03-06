from collections import deque

class TreeNode: 
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

class Node(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []

class Solution:
    def levelOrderTraversal(self, root):
        if root is None:
            return 0

        que = deque([root])
        count = 1
        while que:
            # count += 1
            # if len(que) < 2 ** (count - 1):
            #     return count - 1
            for _ in range(len(que)):
                cur = que.popleft()
                # if (cur.left is None) and (cur.right is None):
                #     return count
                if cur.left:
                    count += 1
                    que.append(cur.left)
                if cur.right:
                    count += 1
                    que.append(cur.right)
        return count




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


print(Solution().levelOrderTraversal(n1))