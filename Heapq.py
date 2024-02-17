import heapq

class Heap:
    def __init__(self):
        self.heap = []
        
    def heappush(self, data):
        heapq.heappush(self.heap, data)
        
    def heappop(self):
        return heapq.heappop(self.heap)
        
    def heappushpop(self, data):
        return heapq.heappushpop(self.heap, data)
        
    def heapreplace(self, data):
        return heapq.heapreplace(self.heap, data)
        
    def nsmallest(self, count):
        return heapq.nsmallest(count, self.heap)
        
    def nlargest(self, count):
        return heapq.nlargest(count, self.heap)

# Example usage:
heap = Heap()

# Push elements onto the heap
heap.heappush(1)
heap.heappush(2)
heap.heappush(3)
heap.heappush(4)
print("Heap after push operations:", heap.heap)

# Pop the smallest element
smallest = heap.heappop()
print("Smallest element popped from heap:", smallest)
print("Heap after pop operation:", heap.heap)

# Push a new element onto the heap and pop the smallest element
new_smallest = heap.heappushpop(2.5)
print("New smallest element after pushpop operation:", new_smallest)
print("Heap after pushpop operation:", heap.heap)

# Replace the smallest element with a new value
replacement = heap.heapreplace(0.5)
print("Value replaced in the heap:", replacement)
print("Heap after replace operation:", heap.heap)

# Get the 2 smallest elements
print("2 smallest elements in the heap:", heap.nsmallest(2))

# Get the 2 largest elements
print("2 largest elements in the heap:", heap.nlargest(2))
