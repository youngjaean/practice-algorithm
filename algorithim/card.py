import heapq

n = int(input())
heap =[]

for _ in range(n):
    heapq.heappush(heap, int(input()))

total = 0 

while len(heap) != 1:
    fir = heapq.heappop(heap)
    sec = heapq.heappop(heap)
    sum_value = fir + sec
    total += sum_value
    heapq.heappush(heap, sum_value)

print(total)

