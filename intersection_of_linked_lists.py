'''Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.'''
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
    
    def __repr__(self):
        return f'{self.val}->{self.next}'


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    a = headA
    b = headB
    d = dict()

    while a:
        d[a] = 1
        a = a.next

    while b:
        if d.get(b, 0):
            return b
        
        b = b.next

    return 


print('\n')
a = ListNode(4, ListNode(1, inter := ListNode(8, ListNode(4, ListNode(5)))))
b = ListNode(5, ListNode(6, ListNode(1, inter)))
print(getIntersectionNode(a, b))

c = ListNode(1, ListNode(9, ListNode(1, inter2 := ListNode(2, ListNode(4)))))
d = ListNode(4, inter2)
print(getIntersectionNode(c, d))

e = ListNode(2, ListNode(6, ListNode(4)))
f = ListNode(1, ListNode(5))
print(getIntersectionNode(None, None))

aa = ListNode(1)
bb = aa
print(getIntersectionNode(aa, bb))



