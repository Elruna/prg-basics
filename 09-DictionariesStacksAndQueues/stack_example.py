import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()
k=0
# adds elements to the top of the stack

cards.put(2)     
cards.put(3)  
cards.put(7)  
cards.put(4)  
cards.put(1)
cards.put(9)
cards.put(8)   
last_two_sum = cards.get() + cards.get()  # Pop last two elements and sum them
print("Sum of the last two numbers:", last_two_sum)
## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())
remaining_sum = 0
# removes and prints elements from the top of the stack
while not cards.empty():
    remaining_sum += cards.get()
    

print(remaining_sum)
"""
Note the order of the printed elements.
The last added element is printed first.
"""
