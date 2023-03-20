class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        return self.backtrack(root, targetSum - root.val)
    
    def backtrack(self, root, targetSum):
        if not root.left and not root.right: 
            if targetSum == 0:
                return True
            else:
                return False

        for child in [root.left, root.right]:
            if child:
                targetSum -= child.val
                if self.backtrack(child, targetSum):
                    return True
                targetSum += child.val
        