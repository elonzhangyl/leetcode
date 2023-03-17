class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def __init__(self, nums):
        self.res = []

    def obtain(self, mid):
        if not mid:
            return
        self.res.append(mid.value)
        if mid.left:
            self.obtain(mid.left.value)
        if mid.right:
            self.obtain(mid.right.value)



print(Solution().question())