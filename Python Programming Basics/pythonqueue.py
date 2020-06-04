from collections import deque 
  
# Initializing a queue 
q = deque() 
  
# Adding elements to a queue 
q.append('a') 
q.append('b') 
q.append('c') 
q.appendleft('k')
  
print("Initial queue") 
print(q) 
  
# Removing elements from a queue 
print("\nElements dequeued from the queue") 
print(q.pop())
print(q.popleft()) 
print(q.popleft()) 
print(q.popleft()) 
  
print("\nQueue after removing elements") 
print(q) 
  
# Uncommenting q.popleft() 
# will raise an IndexError 
# as queue is now empty



#Python Queue Demo
from queue import Queue

q = Queue(maxsize=10)
#print(q.size,q.empty,q.full)

q.put("Ashish")
q.put("Renu")

for i in range(q.qsize()):
    print(q.get())




queue = []

queue.append("Ashish")
queue.append("Renu")
queue.append("Avani")
queue.append("Advik")

print(len(queue))

for i in range(len(queue)):
    print(queue.pop())


