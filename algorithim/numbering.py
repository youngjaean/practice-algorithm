#단지번호 붙이기 

import sys
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(sys.stdin.readline())
a = [list(sys.stdin.readline()) for _ in range(n)]
cnt = 0
apt = []

def dfs(x, y):
    global cnt
    a[x][y] = '0'
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if a[nx][ny] == '1':
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if a[i][j] == '1':
            cnt = 0
            dfs(i, j)
            apt.append(cnt)

print(len(apt))
apt.sort()
for i in apt:
    print(i)

# n = int(input())
# a = [[int(block) for block in input()] for _ in range(n)]
# cnt = 0
# apt = []

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# cnt = 0
# apt = []

# def dfs(x ,y):
#     global cnt
#     cnt += 1
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx < 0 or ny < 0 or nx >= n or ny >= n:
#             continue
#         if a[nx][ny] == '1':
#              dfs(i ,j)

# for i in range(n):
#     for j in range(n):
#         if a[i][j] =='1':
#             cnt = 0
#             dfs(i, j)
#             a.append(cnt)
# print(len(apt))
# apt.sort()
# for i in apt:
#     print(i)