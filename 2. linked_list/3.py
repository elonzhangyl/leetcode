class ListNode():
    
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

def createLinkedList(lst):
    cur_head = None
    for val in reversed(lst):
        cur_head = ListNode(val, cur_head)
    return cur_head

class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        cur = head
        pre = ListNode()
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

lst = [1,2,3,4]
llist = createLinkedList(lst)
llist_r = Solution().reverse(llist)
