class Stack():
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

if __name__ == "__main__":
     
    def is_match(s1,s2):
        if s1 == "(" and s2 == ")":
                return True
        elif s1 == "{" and s2 == "}":
            return True
        elif s1 == "[" and s2 == "]":
            return True
        
    def check_balanced(paren_string):
        index = 0 
        s = Stack() 
        is_balanced = True
        while index < len(paren_string) and is_balanced:
            paren = paren_string[index]
            if paren in "({[":
                s.push(paren)
            else:
                if s.is_empty():
                    is_balanced = False
                else:
                    top = s.pop()
                    if not is_match(top,paren):
                        is_balanced = False
            index +=1

        if s.is_empty and is_balanced:
            return "Balanced"
        else:
            return "NOT Balanced"
    print(check_balanced("[[}}"))



