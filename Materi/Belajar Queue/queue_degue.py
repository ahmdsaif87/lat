from collections import deque

antrian = deque()

def enqueue(item):
    antrian.append(item)

def dequeue():
    antrian.popleft()

def front():
    return antrian(0)

enqueue("Saif")
enqueue("Saup")
enqueue("Saip")
enqueue("Sakip")

deque()

print(antrian)
