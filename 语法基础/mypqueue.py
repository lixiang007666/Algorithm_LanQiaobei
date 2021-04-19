from queue import PriorityQueue

pq=PriorityQueue(maxsize=3)

pq.put(1)
pq.put(2)
pq.put(3)
print(pq.qsize())