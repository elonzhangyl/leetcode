class LinkNode():
    def __init__(self, val, next):
        self.val = val
        self.next = next

def createLinkedList(lst):
    head = None
    for val in reversed(lst):
        head = LinkNode(val, head)
    return head
# get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
# addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
# addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
# addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
# deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
class Solution:
    def reverse(self, head):
        dummy_head = LinkNode(0, head)
        cur = head
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp



lst = [1,2,6,3,4,5,6]
val = 6
head = createLinkedList(lst)
a = Solution().remove(head, val)
while a:
    print(a.val)
    a = a.next