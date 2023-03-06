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
    def len(self, head):
        i = 0
        while head:
            i += 1
            head = head.next
        return i
    
    def reverse_ll(self, head):
        pre = head
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp

    def intersection(self, head10, head20):
        head1 = self.reverse_ll(head10)
        head2 = self.reverse_ll(head20)
        # 反转一个，如果另一个出现变化，那说明二者有交点
        while head1 and head2:
            if head1 == head2:
                return True
            else:
                head1 = head1.next
                head2 = head2.next
        return False
        # len1, len2 = self.len(head1), self.len(head2)
        # if len1 < len2:
        #     head1, head2 = head2, head1
        #     len1, len2 = len2, len1
        # for _ in range(len1 - len2):
        #     head1 = head1.next
        # while head1:
        #     if head1 == head2:
        #         return True
        #     else:
        #         head1 = head1.next
        #         head2 = head2.next
        return False

lst1 = [1,2,3,4,5,6]
head1 = createLinkedList(lst1)
head2 = head1.next.next.next
print(Solution().intersection(head1, head2))