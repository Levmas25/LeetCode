class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}->{self.next}'


def remove_nth_node(head: ListNode, n: int) -> ListNode:
    if not head:
        return 
    
    l = 1
    d = {}
    start = head
    while start:
        d[l] = start
        l += 1
        start = start.next

    pos = l - n - 1
    if pos == 0:
        return head.next
    d[pos].next = None if not d[pos].next.next else d[pos].next.next

    return head


a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
b = ListNode(1)
c = ListNode(1, ListNode(2))

print(remove_nth_node(a, 2))
print(remove_nth_node(b, 1))
print(remove_nth_node(c, 1))

    