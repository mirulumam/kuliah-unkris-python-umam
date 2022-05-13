from email import message
import time
from tracemalloc import start

class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def getItems(self):
        return self.items
    def setTime(self, t):
        self.time = t
    def getTime(self):
        return self.time

def doQueue(q, r):
    start = time.time()
    for m in range(0, r): q.enqueue(m)
    t = time.time() - start
    print("Waktu dibutuhkan queue", t)
    q.setTime(t)
    return q

def doDequeue(q):
    start = time.time()
    for i in range(0, q.size()): q.dequeue()
    t = time.time() - start
    print("Waktu dibutuhkan dequeue", t)
    q.setTime(t)
    return q
