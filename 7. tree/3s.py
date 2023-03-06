
class TreeNode: 
    def __init__(self, value=0):
        self.val = value
        self.left = None
        self.right = None


# 前序遍历-迭代-LC144_二叉树的前序遍历
class Solution:
    def preorderTraversal(self, root):
        stak = [root]
        res = []
        while stak:
            node = stak.pop()
            res.append(node.val)
            if node.right:
                stak.append(node.right)
            if node.left:
                stak.append(node.left)
        return res

    # def postorderTraversal(self, root):
    #     stak = [root]
    #     res = []
    #     while stak:
    #         while node.left:
    #             stak.append(node.left)
    #         cur = stak.pop()
    #         res.append(cur.val)
    #         while node.right:
    #             stak.append(node.right)
    #         cur = stak.pop()
    #         res.append(cur.val)
    #         res.append(node.val)
    #     while stak:
            
    #         if node.right:
    #             stak.append(node.right)
    #         if node.left:
    #             stak.append(node.left)
    #         node = stak.pop()
    #         res.append(node.val)
    #     return res

    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中结点先处理
            result.append(node.val)
            # 左孩子先入栈
            if node.left:
                stack.append(node.left)
            # 右孩子后入栈
            if node.right:
                stack.append(node.right)
        # 将最终的数组翻转
        return result[::-1]


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
    print(Solution().postorderTraversal(n1))
    # print(Solution().inorderTraversal(node1))
    # print(Solution().postorderTraversal(node1))
    # print(Solution().preorderTraversal(node0))
    # print(Solution().preorderTraversal(node11))