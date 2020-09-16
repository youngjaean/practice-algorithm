n = int(input())

block = []
block.append((0, 0, 0, 0))
for i in range(n):
    a, h, w= map(int,(input().split()))
    block.append(((i + 1), a, h, w))

block.sort(key=lambda data: data[3])

dp = [0] * (n +1)
for i in range(1, n + 1):
    for j in range(0, i):
        if block[i][1] > block[j][1]:
            dp[i] = max(dp[i], dp[j] + block[i][2])

max_value = max(dp)
index = n
result = []

while index != 0:
    if max_value == dp[index]:
        result.append(block[index][0])
        max_value -= block[index][2]
    index -= 1

result.reverse()
print(len(result))
[print(i) for i in result]