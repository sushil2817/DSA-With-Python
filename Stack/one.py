# stack => LIFO (Last In First Out)

class stack:
    def __init__(self):
        self.s = []
    
    def length(self):
        print(f"Lenght of Stack: {len(self.s)}")
        return len(self.s)
    
    def push(self,value):
        print(f"Stack: {value}")
        self.s.insert(0,value)
    
    def peek(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.s[0]
    
    def pop(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty")
        else:
            print(f"pop the last element: {self.s.pop(0)}")
            return self.s.pop(0)
        

stk = stack()
stk.push(10);
stk.push(20);
stk.push(30);
stk.push(40);
stk.length()
stk.pop();
print("After pop")
stk.length()