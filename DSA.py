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




class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node 
            return 
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node 
    def display(self):
        temp=self.head
        while temp :
            print(f"data{temp.data}")
            temp=temp.next
            
LL=LinkedList()
LL.insert(10)

LL.insert(20)
LL.display()
        
queue=[]

queue.append(10)
queue.append(20)
print(queue)
#deque
dlt=queue.pop(0)
print(dlt)
#first_elment

first=queue[0]
print(first)

is_empty=len(queue) == 0

print(is_empty)


Size= print(len(queue))      
    








from collections import deque

class Learning_queue:
    def __init__(self): 
        self.queue = deque()
           
    def insert(self, value):
        self.queue.append(value)
        print(value, "added")

    def delete(self):
        if len(self.queue) == 0:
            return print("queue is empty")
        data = self.queue.popleft()
        print(data, "deleted")
         
    def peek(self):
        if len(self.queue) == 0:
            return print("queue is empty")
        data = self.queue[0]
        print("first value is", data)
         
    def is_empty(self):
        if len(self.queue) == 0:
            return print("queue is empty")
        print(len(self.queue) == 0)

    def size(self):
        if len(self.queue) == 0:
            return print("queue is empty")
        print(len(self.queue))


q = Learning_queue()
q.insert(10) # will say "queue is empty" because you check before adding
q.insert(20)
q.size()
q.peek()
q.delete()
q.is_empty()
q.delete()
q.is_empty()    



import queue
val=queue.Queue()
val.put(10)
val.put(20)
val.put(30)
print(val.qsize())
print(val.get())
print(val.qsize())

# prefix
def expression(exp):
    stack=[]
    for char in reversed(exp):
        if char.isdigit():
            stack.append(int(char))
            print(f"{char}value pushed")
        else:
            a=stack.pop()
            b=stack.pop()
            print(f"value poped{a,b}")
            if char == "+":
                stack.append(a+b)
            elif char=="-":
                stack.append(a-b)
            elif char =="*":
                stack.append(a*b)
            elif char == "/":
                stack.append(a/b)
    return stack.pop()
            


print(expression("+52"))

def post_fix(exp):
    
    stack=[]
    for char in exp:
        if char.isdigit():
            stack.append(int(char))
            print(f"{char},added into stack")
            
        else:
            a=stack.pop()
            b=stack.pop()
            
            if char =="+":
                stack.append(a+b)
            elif char == "-":
                stack .append(a-b)
            elif char == "*":
                stack .append(a*b)
            elif char == "/":
                stack .append(a/b)
    return stack.pop()


print(post_fix("52+"))


def valid_paranth(val):
    stack=[]
    expression={')':'(',']':'[','}':'{'}
    
    for char in val :
        if char in '([{':
            stack.append(char)
        
        else :
            if not stack:
                return False
            a=stack.pop()
            if expression[char] != a:
                return False 
                
    return len(stack)==0
    
print(valid_paranth("({[]})"))


arr=[1,2,3,4,5]
prefix=[0]*len(arr)
print(prefix)
prefix[0]=arr[0]
print(prefix)

for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]

print(prefix)

class Linked_list:
    def __init__(self):
       self.head=None

    def add_at_begine(self,data):
        new_node=Node(data)
        temp=self.head
        if temp:
            temp.prev=new_node
            new_node.next=temp
        self.head=new_node

    def add_at_last(self,data):
        new_node=Node(data)
        if self.head is None:
            temp=new_node 
            return 
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp

    def add_between(self,data,value):
        new_node=Node(data)
        temp=self.head
        while temp and temp.data != value:
            temp=temp.next
        if temp is None:
            print("value not found")
            return 
        
        else:
            prev=temp.prev
            prev.next=new_node
            new_node.prev=prev
            new_node.next=temp 
            temp.prev=new_node

    def deletion(self,value):
        temp=self.head
        while temp and temp.data != value:
            temp=temp.next
        if temp is None:
            print("the value is not in ")
            return   
        elif temp==self.head and temp.next is None:
            self.head=None
            return
        elif temp.next is None:
            temp.prev.next=None
            return 
        elif temp == self.head:
            temp.next.prev=None
            self.head=temp.next
            return
        
        temp.next.prev=temp.prev
        temp.prev.next=temp.next
        
        

data=Linked_list()
data.add_at_begine(10)

