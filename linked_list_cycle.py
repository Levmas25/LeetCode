'''Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'{self.val}->{self.next}'
    
    def __str__(self):
        return repr(self)

def hasCicle(head: ListNode) -> bool:
    '''Beats 52%'''
    if not head:
        return False
    
    slow = head
    fast = head.next

    while fast != None and slow != None:
        if slow == fast:
            return True
        
        if slow.next == None or fast.next == None or fast.next.next == None:
            return False
        fast = fast.next.next
        slow = slow.next
        
    return False


a = ListNode(3)
a.next = ListNode(2)
a.next.next = ListNode(0)
b = ListNode(4)
a.next.next.next = b
b.next = a.next

c = ListNode(1)
print(hasCicle(c))


def another_sol(head: ListNode) -> bool:
    '''Same thing just a little better writed'''
    fast = head
    slow = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
        if fast == slow:
            return True

    return False