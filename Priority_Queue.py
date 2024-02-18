import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

pq = PriorityQueue()
pq.push('task1', 5)
pq.push('task2', 1)
pq.push('task3', 3)
print(pq.pop())  
print(pq.pop())  
print(pq.pop())  
