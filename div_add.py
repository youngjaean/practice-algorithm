n = int(input())
l = True

for i in range(0, n):
    if sum(map(int, str(i))) + i == n:
        print(i)
        l = False
        break
if l:
    print(0)

