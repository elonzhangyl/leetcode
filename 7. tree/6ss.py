from collections import deque


class TreeNode: 
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def swithBinaryTree1(self, node:TreeNode) -> list[int]:

        def swithElement(node):
            if node.left:
                swithElement(node.left)
            else:
                return

            if node.right:
                swithElement(node.right)
            else:
                return

            node.left, node.right = node.right, node.left
     
        swithElement(node)
        return node

    def switchBinaryTree2(self, root: TreeNode) -> TreeNode:
        # 这个方法的精髓就在于抓住stack的思想不放松
        if root is None:
            return
        my_stack = [root]
        while my_stack:
            node = my_stack.pop()
            node.left, node.right = node.right, node.left
            if node.right:
                my_stack.append(node.right)
            if node.left:
                my_stack.append(node.left)
        return root

    def switchBinaryTree3(self, root: TreeNode) -> TreeNode:
        que = deque([root])
        while que:
            node = que.popleft()
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)




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

print(Solution().invertTree(n1))