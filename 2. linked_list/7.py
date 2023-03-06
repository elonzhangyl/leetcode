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
    def interception(self, head1: ListNode, head2: ListNode,) -> ListNode:
        cur1, cur2 = head1, head2
        n_node1, n_node2 = 0, 0
        while cur1!=None:
            cur1 = cur1.next
            n_node1 += 1
        while cur2!=None:
            cur2 = cur2.next
            n_node2 += 1

        cur1, cur2 = head1, head2
        if n_node2 > n_node1:
            n_node1, n_node2 = n_node2, n_node1
            cur1, cur2 = cur2, cur1

        for _ in range(n_node1 - n_node2):
            cur1 = cur1.next
        for _ in range(n_node2):
            if cur1.val == cur2.val:
                return cur1
            else:
                cur1 = cur1.next
                cur2 = cur2.next
        return None
        
lst1 = [1,11,2,3]
lst2 = [6,2,3]
llist1 = createLinkedList(lst1)
llist2 = createLinkedList(lst2)

llist_r = Solution().interception(llist1,llist2)
