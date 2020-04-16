from stack import Stack

'''
121
12//2 = ans -> rem
'''
def int_to_bin(number):
    s = Stack()
    binary = ""
    while number > 0 :
        rem = number % 2
        s.push(rem)
        half = number // 2 
        number = half
    while not s.is_empty():
        binary = binary + str(s.pop())       
    return binary
print(int_to_bin(242))
