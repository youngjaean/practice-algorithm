N = int(input())

mod = 10007

num = [[0] * 10 for _ in range(N + 1)]

num[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N + 1):
    for j in range(10):
        for k in range(j, 10):
            num[i][j] += num[i - 1][k]
            

print(sum(num[N]) % mod)
