class stack:
    def __init__(self):
        self.stack=[]
    def push(self,value):
        self.stack.append(value)
    def pop(self,value):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("stack is empty")
            return None
    def isempty(self):
        return len(self.stack)==0
    def printAll(self):
        print(s.top())

s=stack()
s.push(23)
s.push(3)
s.push(2)
s.push(1)

# To print the stack in python
print(s.stack)


