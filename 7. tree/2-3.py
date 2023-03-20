# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 
        self.backtrack([root])
        return self.path
    
    def backtrack(self, children):
        if not children:
            return
        for child in children:
            if child:
                self.path.append(child.val)
                self.backtrack([child.left, child.right])

