from linked_list import Node,LinkedList

def del_dup(self):
    new_head = self.head
    cur_node = self.head
    while cur_node:
        next_node = cur_node.next
        dup = next_node.data
        if cur_node.data == dup.data:
            self.head = dup
            cur_node = None
        else:
            cur_node = cur_node.next
    return new_head

llist_1 = LinkedList()
llist_1.append("1")
llist_1.append("3")
llist_1.append("1")
llist_1.append("6")
llist_1.append("9")
llist_1.del_dup()
llist_1.print_list()