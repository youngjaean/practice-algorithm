n, m = map(int, input().split())

array = []

for _ in range(n):
    array.append(input())

row = [0] * n     
cloum = [0] * m
 
for i in range(n):
    for j in range(m):
        if array[i][j] == 'X':
            row[i] = 1
            cloum[j] = 1

row_count = 0
for i in range(n):
    if row[i] == 0:
        row_count += 1

cloum_count = 0
for j in range(m):
    if cloum[j] == 0:
        cloum_count += 1


print(max(row_count, cloum_count))
