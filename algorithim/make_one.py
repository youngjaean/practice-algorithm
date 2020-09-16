#https://www.acmicpc.net/problem/1463

# save = {1: 0, 2: 1}
# def frog(n):
#     if n in save:
#         return save[n]
#     x = frog(n // 2) + n % 2
#     y = frog(n // 3) + n % 3
#     m = 1 + min(x, y)
#     save[n] = m
#     return m

# n = int(input())
# print(frog(n))



n = int(input())

dp = list()

dp.append(0)
dp.append(0)
dp.append(1)
dp.append(1)

for i in range(4, n):
    dp.append(dp[i - 1] + 1)

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] == min(dp[i], dp[i // 3] + 1)

print(dp[n])