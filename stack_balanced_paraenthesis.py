from stack import Stack

def is_match(top,character):
        if top == "(" and character ==")":
            return True
        elif top == "{" and character =="}":
            return True
        elif top == "[" and character =="]":
            return True
         

def check_balance_parenthesis(paren_string):
    index = 0 
    s = Stack()
    is_balanced = True
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "({[":
               s.push(paren)
        else :
            if s.is_empty():
                is_balanced = False 
            else :
                top = s.pop()
                if not is_match(top,paren):
                    is_balanced = False
        index += 1
            
    if s.is_empty() and is_balanced:
        return "The parenthesis in the string is balanced."
    else:
        return "The parenthesis in the string is not balanced."
           
print(check_balance_parenthesis("]]]{}"))

  
 


