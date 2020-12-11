class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
class Queue(object):
    def __init__(self):
        self.items =[]
    
    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0 

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Binary_Tree(object):
    def __init__(self,root):
        self.root = Node(root)
    

    def print_tree(self,traversal_type):
        if traversal_type == "preorder":
            return self.preorder_traversal(self.root,"")
      
        elif traversal_type == "inorder":
            return self.inorder_traversal(self.root,"")
       
        elif traversal_type == "postorder":
            return self.postorder_travesal(self.root,"")
        
        elif traversal_type == "levelorder":
            return self.levelorder_traversal(self.root)
        
        elif traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_traversal(self.root)
        
        else:
            print(f"Traversal_type {traversal_type} is not present.")
       

    def preorder_traversal(self, start,traversal):
        # Traversal is basically just a string to print
        '''Root -> Left -> Right '''
        if start:
            traversal += (str(start.value)+"-")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        '''Left -> Root -> Right '''
        if start :
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value)+ "-")
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def postorder_travesal(self, start, traversal):
        '''Left -> Right -> Root '''
        if start :
            traversal = self.postorder_travesal(start.left, traversal)
            traversal = self.postorder_travesal(start.right, traversal)
            traversal += (str(start.value)+ "-")
        return traversal
    
    # Level Order Traversal is also known as Breadth First Search
    def levelorder_traversal(self, start):
        if start is None:
            return 
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
                # print("yes")
        return traversal

    def reverse_levelorder_traversal(self, start):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""
        while len(queue)>0:
            node = queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += (str(node.value)) + "-"
        return traversal        

    def height_tree(self, node):
        if node is None:
            return -1
        left_height = self.height_tree(node.left)
        right_height = self.height_tree(node.right)
        return  1 + max(left_height, right_height)

# 1-2-4-5-3-6-7-
# 4-2-5-1-6-3-7
# 4-2-5-6-3-7-1
#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 

# Set up tree:
tree = Binary_Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print("Preorder Traversal",tree.print_tree("preorder"))
print("Inorder Traversal",tree.print_tree("inorder"))
print("Postorder Traversal",tree.print_tree("postorder"))
print("Levelorder Traversal",tree.print_tree("levelorder"))
print("Reverse_Levelorder Traversal",tree.print_tree("reverse_levelorder"))
print("Height of the Tree",tree.height_tree(tree.root))