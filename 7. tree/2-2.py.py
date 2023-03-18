class TreeNode: 
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal(self, node):
        if node:
            self.res.append(node.value)
            for i in [node.left, node.right]:
                self.preorderTraversal(i)
            


    def so(self, root):
        self.preorderTraversal(root)
        return self.res

# driver code
if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    print(Solution().so(n1))
