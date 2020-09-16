n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
total = 0
frist = data[-1]
sec = data[-2]
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         total += frist
#         m -= 1
#     if m == 0:
#         break
#     total += sec
#     m -= 1

count = int(m / (k + 1)) *  k
count += m % (k + 1)

total += frist * count
total += sec * (m - count)
print(total)