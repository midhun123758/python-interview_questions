# https://www.programiz.com/online-compiler/2tLHSdGQfMuZM




class  Stack:
    def __init__(self):
        self.stack=[]
    def __str__(self):
        return f"Stack:{self.stack}"
        
    def push (self,item):
        self.stack.append(item)
        print(item,"pushed in to stack ")
        
    def pop(self):
        if self.is_empty():
            return print("stack is empty ")
        self.stack.pop()
        print("item  poped ")
    def is_empty(self):
        return len(self.stack)==0
    def peek(self):
        if self.is_empty():
            return self.is_empty()
        return self.stack[-1]
        
    def size(self):
        return len(self.stack)
    def display(self):
        print(f"stack {self.stack}")

s=Stack()
s.push(100)
print(s)
s.pop()
print(s)
s.push(200)
s.push(300)
print(s.peek())
print(s)
print(s.size())


# implimentatiom  of stack  use dif moduels

import collections

stack=collections.deque()

stack.append(10)
stack.append(20)
stack.pop()
print(stack)

import queue
stack1 = queue.LifoQueue(2)
stack1.put(10)
stack1.put(20)
stack1.put(20,timeout=1)
print(stack1.get())
print(stack1.get())
print(stack1.get())