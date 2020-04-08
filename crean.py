import sys
n = int(input())
cranes = list(map(int, input().split()))

m = int(input())
boxes = list(map(int, input().split()))

if max(cranes) < max(boxes):
    print(-1)
    sys.exit()


postion = [0] * n
checked = [False] * m

cranes.sort(reverse=True)
boxes.sort(reverse=True)

reslut = 0
count = 0


while True:
    if count == len(boxes):
        break
    for i in range(n):
        while postion[i] < len(boxes):
            if not checked[postion[i]] and cranes[i] >= boxes[postion[i]]:
                checked[postion[i]] = True
                postion[i] += 1
                count += 1
                break
            postion[i] += 1
    reslut += 1

print(reslut)