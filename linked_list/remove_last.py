# remove nth node from the end of a linked list

def remove_nth_from_end(head, n):
    slow = fast = head
    for _ in range(n):
        fast = fast.next

    if fast == None:
        return head.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head
