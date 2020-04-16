class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Used for ptinting the list as well as for generating the length of the list
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
        
    def length_iterative(self):
        cur_node = self.head
        count = 0
        while cur_node:
            cur_node = cur_node.next
            count +=1
        return count 

    def length_reccursive(self, node):
        if node is None:
            return 0 
        return 1 + self.length_reccursive(node.next)

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self,prev_node,data):
        if not prev_node:
            return "There is no such node"
        else:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def delete_node(self,key):
        #Case 1 : When the node to be deleted is the head node
        cur_node = self.head
        if cur_node and cur_node == key:
            self.head = cur_node.next
            cur_node = None
            return

        # Case 2 : When the node is not at the head
        prev = None 
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None
    
    def delete_node_at_position(self,pos):
        cur_node = self.head
        
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return        
        
        count = 0
        prev = None
        while cur_node and count!=pos:
            prev = cur_node
            cur_node = cur_node.next
            count +=1
            
        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node = None

# Testing the functions out here
if __name__ == "__main__":   
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.prepend("E")
    llist.insert_after(llist.head.next, "F")
    print("\nOld List")
    llist.print_list()
    # print(llist.length_iterative())
    print(llist.length_reccursive(llist.head))
    # llist.delete_node("F")
    llist.delete_node_at_position(2)
    print("\nNew List")
    llist.print_list()
    print(llist.length_reccursive(llist.head))
    # print(llist.length_iterative())
