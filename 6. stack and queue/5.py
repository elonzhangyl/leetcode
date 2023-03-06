class Solution:
    def removeDouble(self, s: str) -> str:
        my_stack = []
        for si in s:
            if my_stack and si == my_stack[-1]:
                my_stack.pop()
            else:
                my_stack.append(si)

        return my_stack

Solution().removeDouble('abbaca')
        


