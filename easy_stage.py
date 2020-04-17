#https://www.acmicpc.net/problem/10844

x = int(input())

MOD  = 1000000000

dp = [[0] * 10 for _ in range (101)]
 
dp[1] = [0,1,1,1,1,1,1,1,1,1]
 

for i in range(2, 101):
    dp[i][0] = dp[i - 1][1] 
    dp[i][9] = dp[i - 1][8] 
    for j in range(1, 9):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[x]) % MOD)


 
