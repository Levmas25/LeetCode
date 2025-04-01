'''Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        res = ''
        i = self
        while i != None:
            res += f'{i.val}->'
            i = i.next
        return res

def deleteDublicates(head: ListNode) -> ListNode:
    some = ListNode(-1)
    some.next = head
    
    while head.next != None:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next


    return some.next


b = ListNode(1, ListNode(1, ListNode(1)))
a = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
print(deleteDublicates(b))