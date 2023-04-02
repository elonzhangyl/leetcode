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
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode(next=head)
        cur = pre
        
        # 必须有pre的下一个和下下个才能交换，否则说明已经交换结束了
        while cur.next and cur.next.next:
            temp1 = cur.next
            temp2 = cur.next.next.next

            cur.next = cur.next.next
            cur.next.next = temp1
            cur.next.next.next = temp2

            cur = cur.next.next

        return pre.next


lst = [1,2,3]
llist = createLinkedList(lst)
llist_r = Solution().swapPairs(llist)
