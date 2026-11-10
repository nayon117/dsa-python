# find pairs with given sum in a linked list

def find_pairs_with_sum(head, target_sum):
    if head is None:
        return []

    pairs = []
    seen = set()
    current = head

    while current is not None:
        complement = target_sum - current.data
        if complement in seen:
            pairs.append((complement, current.data))
        seen.add(current.data)
        current = current.next

    return pairs
