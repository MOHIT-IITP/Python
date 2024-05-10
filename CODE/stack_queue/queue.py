queue = []
# inserting element in the queue
queue.append(2)
queue.append(9)
queue.append(3)
queue.append(4)
queue.append(5)

print(queue)

# deleting element from the queue
queue.pop(0)
queue.pop(0)
queue.pop(0)
print(queue)

from collections import deque

hello = deque(['name','age','rollno'])
print(hello)

# remove the last element from the dequeue 
hello.pop()
print(hello)

#remove the first element from the deque
hello.popleft()

#add in the front of the deque
hello.appendleft(34)

#add in the last of the deque
hello.append(20)

