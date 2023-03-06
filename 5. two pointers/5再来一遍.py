class linked_list:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class Solution:
    def reverse_linked(self, head):
        cur = head
        pre = None
        while cur != None:
            # 1, 4 行负责遍历，2，3行负责反转 ； easy!
            temp = cur.next 
            cur.next = pre 
            pre = cur
            cur = temp
        return pre


