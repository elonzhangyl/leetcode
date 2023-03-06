
class Solution:
    def __init__(self):
        self.pre = TreeNode()
        self.count = 0
        self.max_count = 0
        self.result = []

    def findMode(self, root):
        if not root: return None
        self.search_BST(root)
        return self.result
        
    def search_BST(self, cur) -> None:
        if not cur: 
            return None
        self.search_BST(cur.left)
        # 第一个节点
        if not self.pre:
            self.count = 1
        # 与前一个节点数值相同
        elif self.pre.val == cur.val:
            self.count += 1 
        # 与前一个节点数值不相同
        else:
            self.count = 1
        self.pre = cur

        if self.count == self.max_count:
            self.result.append(cur.val)
        
        if self.count > self.max_count:
            self.max_count = self.count
            self.result = [cur.val]	# 清空self.result，确保result之前的的元素都失效
        
        self.search_BST(cur.right)
                
class TreeNode: 
    def __init__(self, value=0):
        self.val = value
        self.left = None
        self.right = None

n1 = TreeNode(5)
n2 = TreeNode(1)
n3 = TreeNode(4)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
n6 = TreeNode(3)
n7 = TreeNode(6)
# n8 = TreeNode(8)
# n9 = TreeNode(9)
n1.left = n2
n1.right = n3
# # n2.left = n4
# # n2.left = n5
n3.left = n6
n3.right = n7
# # n4.right = n8
# n6.right = n9

n1 = Solution().isBinarySearchTree(n1)
# s = Solution()
# s.hasPathSum(n1, 22)
# print(s.res)