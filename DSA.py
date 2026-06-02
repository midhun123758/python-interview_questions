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
stack1 = queue.LifoQueue()
stack1.put(10)
stack1.put(20)
stack1.put(20,timeout=1)
print(stack1.get())



# queue compilation using list

# queue=[]
# element=input("enter the element")
# queue.append(element)
# print(element)
# def defqueue():
#     if not queue:
#         print("quie is empty ")
#     else:
#         element=queue.pop(0)
#         print("element remved from queue")

queue1=[]

element=input("enter your element")
queue1.append(element)
print(queue1)

def defqueue():
    if not queue1:
        print("queue is empty ")
    else:
        element=queue1.pop(0)
        print("element remved from queue")
defqueue()
print(queue1)


from collections import deque
queue2=deque()

element=input("enter you element")
queue2.append(element)
print(queue2)

element=input("enter yes for deleting")
if element=="yes":
    queue2.popleft()
    print(queue2)



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
print(node1.data)
print(node1.next)

node2=Node(20)
node3=Node(30)
node1.next=node2
node2.next=node3
print(node1.next.data)
print(node2.next.data)
print(node3.next)
