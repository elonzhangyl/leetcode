# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = []       
        self.res = []

    def hasPathSum(self, root, targetsum: int) -> bool:
        if self.backtrack([root]):
            return True
    
    def backtrack(self, children, target):
        if not children[0] and not children[-1]:
            if self.res == target:
                return True
            return
        
        for child in children:
            if child:
                self.res += child.val
                if self.backtrack([child.left, child.right], target):
                    return True
                self.res -= child.val