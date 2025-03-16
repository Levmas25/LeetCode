# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
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


def merge_lists(list1: ListNode, list2: ListNode) -> ListNode:
    pointer = ListNode(-1)
    head = pointer

    while list1 and list2:
        if list1.val < list2.val:
            head.next = list1
            list1 = list1.next
        else:
            head.next = list2
            list2 = list2.next
        head = head.next

    head.next = list1 if list1 else list2

    return pointer.next


a = ListNode(1, ListNode(3, ListNode(4)))
b = ListNode(1, ListNode(2, ListNode(3)))

print(merge_lists(a, b))
