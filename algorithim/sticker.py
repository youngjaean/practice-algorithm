
for _ in range(int(input())):
    k = []
    
    n = int(input())
    
    k = [list(map(int, input().split())) for _ in range(2)]
    if n > 1:
        k[0][1] += k[1][0]
        k[1][1] += k[0][0]
    for i in range(2, n):
        k[0][i] += max(k[1][i -1], k[1][i-2])
        k[1][i] += max(k[0][i-1], k[0][i-2])


    print(max(k[0][-1], k[1][-1]))

