# https://www.acmicpc.net/problem/11726,11727

n = int(input())

fir, sec = 0, 1

for _ in range(n):
    fir, sec = sec, 2 * fir + sec

print(sec % 10007)