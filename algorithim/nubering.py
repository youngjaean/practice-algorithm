n = int(input())
k = [int(input()) for _ in range(n)]

k.sort()

result= 0

for i in range(1, len(k) + 1):
    result += abs(i - k[i - 1])

print(result)



    
