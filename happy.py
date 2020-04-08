#https://www.acmicpc.net/problem/15969

n = int(input())
score = list(map(int, input().split()))

print(max(score), min(score))
