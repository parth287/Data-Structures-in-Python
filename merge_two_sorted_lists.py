from linked_list import Node, LinkedList
def merge_sorted(self, llist):
    l1_pointer = self.head
    l2_pointer = llist.head
    s_pointer = None
    if not l1_pointer :
        return l2_pointer
    if not l2_pointer :
        return l1_pointer
    if l1_pointer and l2_pointer:
        if l1_pointer.data <= l2_pointer.data:
            s_pointer = l1_pointer
                .next = l1_pointer
            l1_pointer = s_pointer.next
        else:
            s_pointer = l2_pointer
                l2_pointer = s_pointer.next
        new_head = s_pointer
    while l1_pointer and l2_pointer:
        if l1_pointer.data <= l2_pointer.data:
            s_pointer = l1_pointer
            l1_pointer = s_pointer.next
        else:
            s_pointer.next = l2_pointer
            s_pointer = l2_pointer
            l2_pointer = s_pointer.next
    if not l1_pointer:
        s_pointer.next = l2_pointer
    elif not l2_pointer:
        s_pointer.next = l1_pointer
    return new_head