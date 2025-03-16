'''Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}->{self.next}'


def removeElements(head: ListNode, val: int) -> ListNode:
    if not head:
        return 
    
    cur = head
    prev = ListNode(-1)

    while cur:
        if cur.val == val:
            if not cur.next:
                prev.next = None
                break
            cur.val = cur.next.val
            cur.next = cur.next.next
        else:
            prev = cur
            cur = cur.next

    if head.val == val:
        return 


    return head

a = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
b = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
removeElements(b, 7)



def solution(head: ListNode, val: int) -> ListNode:
    ans = ListNode(0, head)
    dummy = ans

    while dummy:
        while dummy.next and dummy.next.val == val:
            dummy.next = dummy.next.next
        dummy = dummy.next
    
    return ans.next