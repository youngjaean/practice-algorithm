#https://www.acmicpc.net/problem/16769

# bucket1_cap, bucket1 = map(int, input().split()) 
# bucket2_cap, bucket2 = map(int, input().split())
# bucket3_cap, bucket3 = map(int, input().split())


# for _ in range(100):

#     if bucket2 + bucket1 <= bucket2_cap:
#         bucket2 += bucket1
#         bucket1 = 0 
#     else: 
#         bucket1 -= bucket2_cap - bucket2
#         bucket2 = bucket2_cap

#     if bucket3 + bucket2 <= bucket3_cap:
#         bucket3 += bucket2
#         bucket2 = 0
#     else: 
#         bucket2 -= bucket3_cap - bucket3
#         bucket3 = bucket3_cap 

#     if bucket3 + bucket1 <= bucket1_cap:
#         bucket1 += bucket3
#         bucket3 = 0
#     else: 
#         bucket3 -= bucket1_cap - bucket1
#         bucket1 = bucket1_cap  


# print(bucket1)
# print(bucket2)
# print(bucket3)


C, M = list(), list()

for i in range(3):
    a, b = map(int, input().split())
    C.append(a)
    M.append(b)

for i in range(100):
    idx = i % 3
    nxt = (idx + 1) % 3
    M[idx], M[nxt] = max(M[idx] - (C[nxt] - M[nxt]), 0), min(C[nxt], M[nxt] + M[idx])


for i in M:
    print(i)




