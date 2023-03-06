class ListNode():
    
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

def createLinkedList(lst):
    cur_head = None
    for val in reversed(lst):
        cur_head = ListNode(val, cur_head)
    return cur_head

class Node(object):
    def __init__(self, x=0):
        self.val = x
        self.next = None

class LinkedList(object):

    def __init__(self):
        self.head = Node()
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        cur = self.head.next
        while(index):
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    def addAtTail(self, val):
        new_node = Node(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        self.size += 1
    
    def addAtIndex(self, idx, val):
        if idx < 0 | idx > self.size:
            return

        new_node = Node(val)
        cur = self.head
        for i in range(idx):
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node
        self.size += 1

    def deleteAtIndex(self, idx):
        if idx < 0 | idx > self.size:
            return
        cur = self.head
        while idx:
            cur = cur.next
            idx -= 1
        cur.next = cur.next.next
        self.size -= 1



# lst = [1,2,3]
# linked_list = createLinkedList(lst)
linked_list = LinkedList()
print(linked_list.get(0))
linked_list.addAtHead(1)