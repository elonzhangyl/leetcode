from collections import deque


class solution:
    def haspathsum(self, root, targetsum: int) -> bool:
        def isornot(root, targetsum) -> bool:
            if (not root.left) and (not root.right) and targetsum == 0:
                return True  # 遇到叶子节点，并且计数为0
            if (not root.left) and (not root.right):
                return False  # 遇到叶子节点，计数不为0
            if root.left:
                targetsum -= root.left.val  # 左节点
                if isornot(root.left, targetsum): return True  # 递归，处理左节点
                targetsum += root.left.val  # 回溯
            if root.right:
                targetsum -= root.right.val  # 右节点
                if isornot(root.right, targetsum): return True  # 递归，处理右节点
                targetsum += root.right.val  # 回溯
            return False

        if root == None:
            return False  # 别忘记处理空treenode
        else:
            return isornot(root, targetsum - root.val)


        return sum
        
                
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