# remove duplicates from sorted linked list 

def remove_duplicates(head):
    if head is None:
        return None

    current = head

    while current is not None and current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next  # Skip the duplicate node
        else:
            current = current.next  # Move to the next node

    return head
