from stack import Stack

def reverse_string(s, string):
    rev_string = ""
    for i in string:
        s.push(i)
    while not s.is_empty():
        rev_string = rev_string + str(s.pop())

    return rev_string

input_str  = ("Hello")
s = Stack()
print(reverse_string(s,input_str))

#BOnus Tip. 
# One Liner for rev  a string or a number
print(input_str[::-1])