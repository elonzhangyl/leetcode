class linked_node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

def createLinkedList(lst):
    cur_head = None
    for val in reversed(lst):
        cur_head = linked_node(val, cur_head)
    return cur_head

class Solution:
    def has_circle(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                p = head
                q = slow
                while p != q:
                    p = p.next
                    q = q.next
                return p.value
        return None


lst1 = [1,2,3,4,5,6]
head1 = createLinkedList(lst1)
head1.next.next.next.next.next.next = head1.next.next.next
print(Solution().has_circle(head1))