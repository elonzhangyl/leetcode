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
    def circleFounder(self, head: ListNode) -> ListNode:
        cur = head
        nodes = [cur]
        pos = -1
        while cur.next:
            pos += 1
            cur = cur.next
            nodes.append(cur)                
            if cur.next in nodes:
                print('yes')
                return pos
        return -1

node4 = ListNode(4,None)
node3 = ListNode(3,node4)
node2 = ListNode(2,node3)
node1 = ListNode(1,node2)
node4.next = node2

llist_r = Solution().circleFounder(node1)
