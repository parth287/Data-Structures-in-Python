class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Used for printing the list as well as for generating the length of the list
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

    # Swapping throught the .next part of the node 
    def swap_nodes(self,key1 ,key2):
        if key1 == key2:
            return
        
        prev1 = None 
        cur_node1 = self.head
        while cur_node1 and cur_node1.data != key1:
            prev1 = cur_node1
            cur_node1 = cur_node1.next
        
        prev2 = None
        cur_node2 = self.head
        while cur_node2 and cur_node2.data != key2:
            prev2 = cur_node2
            cur_node2 = cur_node2.next
        
        if not cur_node1 or not cur_node2:
            return
        
        if prev1:
            prev1.next = cur_node2
        else:
           self.head =  cur_node2
        
        if prev2:
            prev2.next = cur_node1
        else:
            self.head = cur_node1 

        cur_node1.next, cur_node2.next = cur_node2.next, cur_node1.next           

    # Swapping through the data part of the node
    def swap_nodes_data(self, key1, key2):
        if key1 == key2 :
            return
        cur_node = self.head
        copy1, copy2 = None , None
        while cur_node :
            if cur_node.data == key1:
                copy1 = cur_node # Key 1 found
            elif cur_node.data == key2:
                copy2 = cur_node # Key 2 found
            cur_node = cur_node.next
        if copy1 and copy2:
            copy1.data, copy2.data = copy2.data , copy1.data

    def reverse_list(self):
        prev = None 
        cur_node = self.head
        while cur_node :
            nxt = cur_node.next
            cur_node.next = prev 
            prev = cur_node
            cur_node = nxt
        self.head = prev 
    
    def reverse_list_reccursive(self):
        def reverse_reccursive(cur_node, prev):
            if not cur_node:
                return prev
            nxt = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = nxt
            return reverse_reccursive(cur_node, prev)
        self.head = reverse_reccursive(cur_node = self.head , prev = None)

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        
        if not p :
            return q
        if not q :
            return p
        
        if p and q:
            if p.data <= q.data:
                s= p
                p = s.next
            else:
                s= q
                q = s.next
            new_head = s
        
        while p and q:
            if p.data <= q.data:
                s.next = p
                s= p
                p = s.next
            else:
                s.next = q
                s= q
                q = s.next
        
        if not p:
            s.next = q
        if not q:
            s.next = p
        self.head = new_head
        llist.head = None
        return new_head
    
    def del_dup(self):
        cur_node = self.head
        prev = None
        dup = {}
        while cur_node:
            if cur_node.data in dup:
                prev.next = cur_node.next
                cur_node = None
            else:
                dup[cur_node.data] = 1
                prev = cur_node
            cur_node = prev.next
    
    def n_from_last_node(self, n):
        # Method 1
        cur_node = self.head
        total_length = self.length_iterative()
        while cur_node:
            if total_length == n:
                print(cur_node.data)
                return cur_node
            total_length -= 1
            cur_node = cur_node.next
        if not cur_node:
            return f"{str(n)} is greater than the length of the string."

        # Method 2:
        p = self.head
        q = self.head 
        count = 0
        while q and count < n :
            q = q.next
            count += 1
        if not q :
            return f"{str(n)} is greater than the length of the string."
        if p and q :
            p = p.next
            q = q.next
        return p.data

    def count_occurences(self, n):
        cur_node = self.head
        count = 0
        while cur_node:
            if cur_node.data == str(n):
                cur_node = cur_node.next
                count += 1
            else:
                cur_node = cur_node.next
        return count

    def rotate(self, n):
        cur_node = self.head
        prev = None
        count = 1
        while cur_node and count < int(n) :
            prev = cur_node
            cur_node = cur_node.next
            count +=1
        new_head = cur_node
        prev.next = None
        if not prev:
            return f"{str(n)} is larger than the string size."
        else:
            while cur_node:
                prev = cur_node 
                cur_node = cur_node.next
            prev.next = self.head
            self.head = new_head
        return new_head

    def is_palindrome(self):
        cur_node = self.head
        check =""
        while cur_node:
            check = check + str(cur_node.data)
            cur_node = cur_node.next
        return check == check[::-1]

    def tail_to_head(self):
        cur_node = self.head
        prev = None
        while cur_node.next:
            prev = cur_node
            cur_node = cur_node.next
        cur_node.next = self.head
        prev.next =None
        self.head = cur_node
        return self.head

    def sum_of_2lists(self, list2):
        cur_node = self.head 
        ans1 = 0
        while cur_node:
            ans1 = ans1 + int(cur_node.data)
            cur_node = cur_node.next
        cur_node2 = list2.head
        ans2 = 0 
        while cur_node2:
            ans2 = ans2 + int(cur_node2.data)
            cur_node2 = cur_node2.next
        return ans1+ans2
        
# Testing the functions out here
if __name__ == "__main__":   
    llist_1 = LinkedList()
    llist_2 = LinkedList()

    llist_1.append("1")
    llist_1.append("3")
    llist_1.append("3")
    llist_1.append("3")
    llist_1.append("3")
    llist_1.append("9")
    llist_1.append("1")
    # llist_1.del_dup()
    # llist_1.n_from_last_node(2)
    # print(llist_1.count_occurences(9))
    # llist_1.rotate(4)
    # print(llist_1.is_palindrome())
    # llist_1.tail_to_head()
    print(llist_1.sum_of_2lists(llist_2))

    llist_2.append("2")
    llist_2.append("4")
    llist_2.append("7")
    llist_2.append("8")
    llist_2.append("10")

    # llist_1.merge_sorted(llist_2)
    # llist_1.print_list()


    # llist = LinkedList()
    # llist.append("A")
    # llist.append("B")
    # llist.append("C")
    # llist.prepend("E")
    # llist.insert_after(llist.head.next, "F")
    # print("\nOld List")
    # llist.print_list()
    # # print(llist.length_iterative())
    # print(llist.length_reccursive(llist.head))
    # # llist.delete_node("F")
    # # llist.delete_node_at_position(2)
    # print("\nNew List")
    # # llist.swap_nodes_data("E", "C")
    # # llist.swap_nodes("C", "E")
    # # llist.reverse_list()
    # llist.reverse_list_reccursive()
    # llist.print_list()
    # print(llist.length_reccursive(llist.head))
    # # print(llist.length_iterative())

