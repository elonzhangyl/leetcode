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
    def deleteNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(next=head)
        cur_fast, cur_slow = dummy_head, dummy_head
        while n!=0:
            cur_fast = cur_fast.next
            n -= 1
        while cur_fast.next!=None:
            cur_fast = cur_fast.next
            cur_slow = cur_slow.next
        
        cur_slow.next = cur_slow.next.next
        return dummy_head.next
        
lst = [1,2,3]
llist = createLinkedList(lst)
llist_r = Solution().deleteNthFromEnd(llist,3)
