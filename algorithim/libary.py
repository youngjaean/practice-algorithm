import heapq

n, m = map(int, input().split())

array = list(map(int, input().split()))

postive = []
negative = []

largest = max(max(array), -min(array))

for i in array:
    if i > 0:
        heapq.heappush(postive, -i)
    else:
        heapq.heappush(negative, i)

result = 0

while postive:

    result += heapq.heappop(postive)
    for _ in range(m - 1):
        if postive:
            heapq.heappop(postive)

while negative:
    result += heapq.heappop(negative)
    for _ in range(m - 1):
        if negative:
            heapq.heappop(negative)

print(-result * 2 - largest)