# delete all occurances of a key

def delete_occurances(head, key):
    if head is None:
        return None

    # Create a dummy node to handle edge cases
    dummy = Node(0)
    dummy.next = head
    current = dummy

    while current.next is not None:
        if current.next.data == key:
            # Skip the node with the matching key
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next
