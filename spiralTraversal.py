
#   write a function that that takes a head of a singly Linked List and rverves the list in place

def reverseList(head):
    if head is None:
        return None
    if head.next is None:
        return head
    current = head
    next = head.next
    while next is not None:
        current.next = next.next
        next.next = head
        head = next
        next = current.next
    return head