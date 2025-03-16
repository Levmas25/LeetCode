class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}->{self.next}'
    

def reverseList(head: ListNode) -> ListNode:
    if not head:
        return 
    
    if head.next is None:
        return head
    
    rest = head.next
    temp = ListNode(-1)
    head.next = None
    while temp:
        temp = rest.next
        rest.next = head
        head = rest
        rest = temp

    return head


def solution(head: ListNode) -> ListNode:
    prev = None  # Previous node starts as None
    curr = head  # Current node starts at the head

    # Traverse the list
    while curr is not None:
        next_node = curr.next  # Save the next node
        
        curr.next = prev  # Reverse the link
        
        # Move pointers forward
        prev = curr  # Move prev to the current node
        curr = next_node  # Move curr to the next node

    # prev is now the new head of the reversed list
    return prev



a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
b = ListNode(1, ListNode(2))
print(reverseList(a))
print(reverseList(b))
print(reverseList(None))