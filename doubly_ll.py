class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
    
    def append(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.next =  None
            new_node.prev = curr

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            curr = self.head
            new_node = Node(data)
            new_node.next = curr
            curr.prev = new_node
            new_node.prev = None
            self.head = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def add_before(self, data, key):
        curr = self.head
        while curr:
            if curr.data == key and curr.next is None:
                self.prepend(data)
                return
            elif curr.data == key:
                new_node = Node(data)
                prev= curr.prev
                curr.prev = new_node
                prev.next = new_node
                new_node.next = curr
                new_node.prev = prev
            curr = curr.next
             
    def add_after(self, data, key):
        curr = self.head
        while curr:
            if curr.data == key and curr.next is None:
                self.append(data)
                return
            elif curr.data == key:
                new_node = Node(data)
                nxt = curr.next
                curr.next = new_node
                nxt.prev = new_node
                new_node.next = nxt
                new_node.prev = curr
            curr = curr.next

    def delete(self,key):
        curr = self.head
        while curr:
            if curr.data == key and curr == self.head:
                if not curr.next :
                    curr = None
                    self.head = None
                    return
                else:
                    nxt = curr.next 
                    nxt.prev = None
                    curr = None
                    curr.next = None
                    return
            elif curr.data == key:
                if curr.next:
                    nxt = curr.next 
                    prev = curr.prev
                    prev.next = nxt
                    nxt.prev = prev
                    curr = None
                    curr.next = None
                    curr.prev = None
                    return
                else:
                    prev = curr.prev
                    prev.next = None
                    curr.prev = None
                    curr = None
                    return
            curr = curr.next
    
    def delete_node(self,node):
        curr = self.head
        while curr:
            if curr == node and curr == self.head:
                if not curr.next :
                    curr = None
                    self.head = None
                    return
                else:
                    nxt = curr.next 
                    nxt.prev = None
                    curr = None
                    curr.next = None
                    self.head = nxt
                    return
            elif curr == node:
                if curr.next:
                    nxt = curr.next 
                    prev = curr.prev
                    prev.next = nxt
                    nxt.prev = prev
                    curr.next = None
                    curr.prev = None
                    curr = None
                    return
                else:
                    prev = curr.prev
                    prev.next = None
                    curr.prev = None
                    curr = None
                    return
            curr = curr.next

    def reverse(self):
        curr = self.head 
        tmp = None
        while curr :
            tmp = curr.prev
            curr.prev = curr.next
            curr.next = tmp
            curr = curr.prev
        if tmp :
            self.head = tmp.prev

    def remove_dup(self):
        curr = self.head
        seen = {}
        # seen = []
        while curr:
            if curr.data not in seen:
                seen[curr.data] = 1
                # seen.append(curr.data)
                curr = curr.next
            else:
                nxt = curr.next
                self.delete_node(curr)
                curr = nxt 

    def sum_pairs(self, sum_value):
        p = self.head 
        pairs = []
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_value:
                    pairs.append(f"({p.data},{q.data})")
                q = q.next
            p = p.next
        return pairs

ddlist = DoublyLinkedList()
# ddlist.append(2)
ddlist.append(2)
ddlist.append(8)
ddlist.append(7)
ddlist.append(5)
# ddlist.append(12)
# ddlist.prepend(1)
# ddlist.add_after(6,5)
# ddlist.add_before(4,5)
# ddlist.reverse()
# ddlist.remove_dup()
print(ddlist.sum_pairs(10))
# ddlist.print_list()

