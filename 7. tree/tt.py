class TreeNode: 
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def levelOrderTraversal(self, root):
        if not root:
            return
        que = [root]
        while que:
            size_ = len(que)
            for _ in range(size_):
                node = que.pop(0)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                if que:
                    node.next = que[0]
                else:
                    node.next = None
        return root

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