# find length of loop in linked list

def find_length(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = slow.next
            length = 1
            while slow != fast:
                slow = slow.next
                length += 1
            return length

    return 0
