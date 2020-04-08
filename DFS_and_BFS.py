# from collections import deque
# def dfs(v):
#     print(v, end = ' ')
#     visted[v] = True
#     for e in adj[v]:
#         if not visted[e]:
#             dfs(e)
        

# def bfs(v):
#     q = deque([v])
#     while q:
#         v = q.popleft()
#         if not visted[v]:
#             visted[v] = True
#             # print(v, end=' ')
#             for e in adj[v]:
#                 if not visted[e]:
#                     q.append(e)
#     return q

from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        
        if not visted[v]:
            visted[v] = True
            # print(v, end = ' ')
            for e in adj[v]:
                if not visted[e]:
                    q.append(e)
            need_visted.append(v)
    return need_visted

def dfs(v):
    need_visted.append(v)
    # print(v, end=' ')
    visted[v] = True
    for e in adj[v]:
        if not visted[e]:
            dfs(e)
    return need_visted

n, m, v = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()

visted = [False] * (n + 1)
need_visted = []
for i in dfs(v):
    print(i, end= ' ')
print()
visted = [False] * (n + 1)
need_visted = []
print(bfs(v))
