class Solution:
    def evlRPN(self, exprs: list) -> int:
        my_stack = []
        for index, s in enumerate(exprs):
            if s not in ['+','-','*','/']:
                my_stack.append(s)
            else:
                num1, num2 = my_stack.pop(), my_stack.pop()
                my_stack.append(str(eval(num2+s+num1)))
        return my_stack

            
s = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Solution().evlRPN(s)