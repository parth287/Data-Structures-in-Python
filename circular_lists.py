class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList():
    def __init__(self):
        self.head = None
    
    def append(self,data):
        if not self.head :
            self.head = Node(data)
            self.head.next = self.head
        else:
            new = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new
            new.next = self.head
        
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def prepend(self, data):
        new = Node(data)
        cur = self.head
        new.next = self.head
        if not self.head:
            new.next = new.node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new
            self.head = new

    def remove_node(self, key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next 
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next

    def __len__(self):
        cur = self.head
        count = 1
        while cur.next != self.head:
            count += 1
            cur =cur.next
        return count

    def split(self):

        if self.__len__() == 0:
           return None
        if self.__len__() == 1:
            return self.head 

        cur = self.head
        prev = None
        half = self.__len__() // 2  
        count = 0      
        
        while cur and count < half:
            prev = cur
            cur = cur.next
            count += 1

        prev.next = self.head 
        split_cclist = CircularLinkedList()
        
        while cur.next != self.head:
            split_cclist.append(cur.data)
            cur = cur.next
        split_cclist.append(cur.data)
        self.print_list()
        print("\nSplitted list\n")
        return split_cclist.print_list()
          


if __name__ == "__main__":
    cllist_1 = CircularLinkedList() 
    cllist_1.append("1")
    cllist_1.append("2")
    cllist_1.append("3")
    cllist_1.append("4")
    cllist_1.append("5")
    cllist_1.prepend("0")
    # cllist_1.remove_node("3")
    cllist_1.split()
    # cllist_1.print_list()
